class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency


class MinHeap:
    
    def __init__(self):
        self.data = []

    def insert(self, patient):
        self.data.append(patient)
        # use heapify_up starting at the last index
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
      
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break

    # keep backward-compatible alias if other code uses the old name
    def _bubble_up(self, index):
        return self.heapify_up(index)

    def extract_min(self):
        if len(self.data) == 0:
            print("⚠️ The queue is empty. No patients to extract.")
            return None
        if len(self.data) == 1:
            return self.data.pop()

        min_patient = self.data[0]
        self.data[0] = self.data.pop()
        # use heapify_down starting at index 0
        self.heapify_down(0)
        return min_patient

    def heapify_down(self, index):
        n = len(self.data)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < n and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    # keep backward-compatible alias if other code uses the old name
    def _bubble_down(self, index):
        return self.heapify_down(index)

    def peek(self):
        if len(self.data) == 0:
            print("⚠️ The queue is empty. No patients to peek.")
            return None
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def remove_min(self):
        return self.extract_min()
