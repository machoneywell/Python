import heapq
from typing import List
import csv


class Node:
    """
    A generic class implementing the common functionality of nodes and switches.
    The node_id is used to represent the node.

    The routes is a dictionary that is used to forward a packet.
    The destination is stored as the key in the dictionary and the value is the next hop.
    Given a packet, you can retrieve the next by looking for its destination in routes.

    """

    def __init__(self, node_id: str):
        self.node_id = node_id
        self.routes = {}

    def add_route(self, destination, next_hop):
        self.routes[destination] = next_hop

    def next_hop(self, destination):
        if self == destination:
            return self
        return self.routes[destination]


class Packet:
    """
    Represent a packet. Currently, a packet includes only the source and destination, which are
    usually included in the header of the packet. A unique packet id is given to each packet
    upon its creating.
    """
    cnt: int = 0

    def __init__(self, source: Node, destination: Node):
        self.packet_id = Packet.cnt
        Packet.cnt += 1
        self.source = source
        self.destination = destination

    def __str__(self):
        return f'P[{self.packet_id},{self.source.node_id}->{self.destination.node_id}]'


class Host(Node):
    """
    A host includes a FIFO queue that stores the packets to be transmitted
    """

    def __init__(self, node_id):
        super().__init__(node_id)
        self.output_queue = []

    def __str__(self):
        return f'{self.node_id:2s} queue={[p.packet_id for p in self.output_queue]}'


class Switch(Node):
    """
    The class emulate the behavior of a switch/router.
    Note that unlike a host, the switch has both an input and an output queue.
    """

    def __init__(self, node_id, processing_delay=0):
        super().__init__(node_id)
        self.input_queue: List[Packet] = []
        self.output_queue: List[Packet] = []
        self.processing_delay = processing_delay

    def __str__(self):
        return f'{self.node_id:2s} in={[p.packet_id for p in self.input_queue]} out={[p.packet_id for p in self.output_queue]}'


class Event:
    """
    This class holds the information about the events that will be interpreted by the
    simulator. The event has the following state
    - target_node - the node that needs to handle the packet
    - event_type - it can be either ENQUEUE, TRANSMIT, PROPAGATE, RECEIVE
    - time - the time when the event will be executed
    - packet - the packet associated with the event (can be None)
    - event_id - the id of the event

    """
    ENQUEUE = 0
    TRANSMIT = 1
    PROPAGATE = 2
    RECEIVE = 3

    cnt = 0

    def __init__(self, event_type: int, target_node: Node, packet: Packet = None, time: int = None):
        assert (0 <= event_type <= 3)
        self.target_node = target_node
        self.event_type = event_type
        self.time = time
        self.packet = packet
        self.event_id = Event.cnt
        Event.cnt += 1

    def type_to_str(self):
        if self.event_type == Event.ENQUEUE:
            return 'ENQUEUE'
        elif self.event_type == Event.TRANSMIT:
            return 'TRANSMIT'
        elif self.event_type == Event.PROPAGATE:
            return 'PROPAGATE'
        elif self.event_type == Event.RECEIVE:
            return 'RECEIVE'
        else:
            raise Exception('Unknown event type')

    def __str__(self):
        return f'{self.time:4d} {self.type_to_str():12s} {self.target_node.node_id} pkt={str(self.packet)}'


class Simulator:
    """
    The main simulator class.
    """

    def __init__(self, transmission_delay=10, propagation_delay=1):
        self.event_queue: List[Event] = []
        self.transmission_delay: int = transmission_delay
        self.propagation_delay: int = propagation_delay
        self.clock = 0
        self.nodes = {}
        self.event_log = []

    def schedule_event_after(self, event: Event, delay: int):
        """
        Schedules an event to be executed in the future

        :param event:
        :param delay: - the delay after which the event will be executed
        :return:
        """
        event.time = self.clock + delay
        heapq.heappush(self.event_queue, (event.time, event.cnt, event))

    def run(self, output_filename="output.csv"):
        """
        Runs the simulator.

        :return:
        """
        print('Starting simulation')
        while len(self.event_queue) > 0:
            self.clock, _, event = heapq.heappop(self.event_queue)

            print(f'{str(event)}')
            self.handle_event(event)

        # Write to CSV
        with open(output_filename, "w", newline="") as f:
            writer = csv.writer(f)
            if "single" in output_filename:
                writer.writerow(["Seq Num", "Queue @A", "Transmit @A", "Propagate @A", "Receive @B"])
                writer.writerows([[entry[0], entry[2], entry[3], entry[4], entry[5]] for entry in self.event_log])
            else:
                writer.writerow(["Seq Num", "Source", "Queue @src", "Transmit @src", "Receive @C", "Transmit @C", "Receive @D"])
                writer.writerows(self.event_log)

    def handle_event(self, event):
        """
        Handles the execution of the events. You must implement this

        :param event:
        :return:
        """
        if event.packet:
            log_entry = None
            for entry in self.event_log:
                if entry[0] == event.packet.packet_id:
                    log_entry = entry
                    break

            if not log_entry:
                log_entry = [event.packet.packet_id, None, None, None, None, None, None]
                self.event_log.append(log_entry)

            if event.event_type == Event.ENQUEUE:
                log_entry[2] = self.clock  # Queue time
            elif event.event_type == Event.TRANSMIT:
                log_entry[3] = self.clock  # Transmission start time
            elif event.event_type == Event.RECEIVE and event.target_node.node_id == "C":
                log_entry[4] = self.clock  # Packet received at switch C
            elif event.event_type == Event.TRANSMIT and event.target_node.node_id == "C":
                log_entry[5] = self.clock  # Packet transmitted from C
            elif event.event_type == Event.RECEIVE and event.target_node.node_id == "D":
                log_entry[6] = self.clock  # Packet received at final destination D

        if event.event_type == Event.ENQUEUE:
            event.target_node.output_queue.append(event.packet)
            if len(event.target_node.output_queue) == 1:
                self.schedule_event_after(Event(Event.TRANSMIT, event.target_node, event.packet), self.transmission_delay)

        elif event.event_type == Event.TRANSMIT:
            next_hop = event.target_node.next_hop(event.packet.destination)
            self.schedule_event_after(Event(Event.PROPAGATE, next_hop, event.packet), self.propagation_delay)

            if len(event.target_node.output_queue) > 1:
                next_packet = event.target_node.output_queue.pop(0)
                self.schedule_event_after(Event(Event.TRANSMIT, event.target_node, next_packet), self.transmission_delay)

        elif event.event_type == Event.PROPAGATE:
            self.schedule_event_after(Event(Event.RECEIVE, event.target_node, event.packet), 0)

        elif event.event_type == Event.RECEIVE:
            if event.target_node == event.packet.destination:
                print(f"Packet {event.packet} received by {event.target_node.node_id}.")
            else:
                next_hop = event.target_node.next_hop(event.packet.destination)
                next_hop.output_queue.append(event.packet)
                if len(next_hop.output_queue) == 1:
                    self.schedule_event_after(Event(Event.TRANSMIT, next_hop, event.packet), self.transmission_delay)


    def new_node(self, node_id: str):
        if node_id in self.nodes:
            raise Exception('Node already added')
        node = Host(node_id)
        self.nodes[node_id] = node
        return node

    def new_switch(self, str_id, processing_delay):
        if str_id in self.nodes:
            raise Exception('Node already added')
        switch = Switch(str_id, processing_delay=processing_delay)
        self.nodes[str_id] = switch
        return switch


def link_experiment():
    sim = Simulator()
    A, B = sim.new_node('A'), sim.new_node('B')
    A.add_route(B, B)

    for _ in range(2):
        packet = Packet(A, B)
        sim.schedule_event_after(Event(Event.ENQUEUE, A, packet), 0)

    sim.run("single_link.csv")


def switch_experiment():
    sim = Simulator()
    A, B, C, D = sim.new_node('A'), sim.new_node('B'), sim.new_switch('C', processing_delay=1), sim.new_node('D')
    A.add_route(D, C)
    B.add_route(D, C)
    C.add_route(D, D)

    for t in range(0, 10000, 1000):
        for _ in range(10):
            packet = Packet(A, D)
            sim.schedule_event_after(Event(Event.ENQUEUE, A, packet), t)

    for t in range(0, 10000, 500):
        for _ in range(2):
            packet = Packet(B, D)
            sim.schedule_event_after(Event(Event.ENQUEUE, B, packet), t)
    
    sim.run("switch.csv")


if __name__ == '__main__':
    link_experiment()  
    switch_experiment()
