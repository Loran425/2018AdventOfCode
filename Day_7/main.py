from string import ascii_uppercase
from dataclasses import dataclass


@dataclass
class Worker:
    number: int
    task: str = '.'
    started: int = None
    duration: int = None
    busy: bool = False

    def update(self, time):
        if self.busy:
            if time >= self.started + self.duration:
                finished = self.task
                self.task = '.'
                self.started = None
                self.duration = None
                self.busy = False
                return finished
        else:
            return None

    def assign(self, task_id, time):
        self.task = task_id
        self.started = time
        self.duration = ord(task_id) - 4
        self.busy = True

    def __str__(self):
        return self.task


def main():
    ###########################################################################
    # INPUT PROCESSING
    ###########################################################################

    with open('./input.txt', mode='r') as f:
        data = []
        for line in f:
            entry = line.split()
            entry = [entry[1], entry[7]]
            data.append(entry)

    prereqs = {char: [] for char in ascii_uppercase}

    for entry in data:
        prereq, step = entry
        prereqs[step].append(prereq)

    task_list = prereqs.copy()
    for t in task_list:
        task_list[t] = prereqs[t].copy()

    ###########################################################################
    # PART 1
    ###########################################################################
    order = ""
    while prereqs:
        available_steps = [step for step in prereqs if not prereqs[step]]
        available_steps.sort()
        current_step = available_steps[0]
        order += current_step
        del prereqs[current_step]
        for step in prereqs:
            if current_step in prereqs[step]:
                prereqs[step].remove(current_step)

    ###########################################################################
    # PART 2
    ###########################################################################
    num_workers = 5
    workers = [Worker(i) for i in range(num_workers)]
    time = 0
    completed = ""
    while True:
        busy_workers = [worker for worker in workers if worker.busy]
        for worker in busy_workers:
            finished_task = worker.update(time)
            if finished_task:
                for task in task_list:
                    if finished_task in task_list[task]:
                        task_list[task].remove(finished_task)
                        if finished_task not in completed:
                            completed += finished_task

        tasks = [task for task in task_list if not task_list[task]]
        tasks.sort(key=lambda x: task_list[x])

        free_workers = [worker for worker in workers if not worker.busy]
        for worker in free_workers:
            if tasks and not worker.busy:
                worker.assign(tasks[0], time)
                del task_list[tasks.pop(0)]

        if not task_list and not any([worker.busy for worker in workers]):
            break
        print(f"[{str(time).zfill(3)}] \t{' '.join([str(w) for w in workers])} \t{completed}")
        time += 1

    print(f'Final task order (1 worker): {order}')
    print(f'5 Workers take {time} seconds to complete the tasks')


if __name__ == '__main__':
    main()