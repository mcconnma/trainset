import multiprocessing
import time

class Test:

	@staticmethod
	def worker(procnum, return_dict):
			'''worker function'''
			print str(procnum) + ' represent!'
			for i in range(10000):
				pass
			return_dict[procnum] = procnum

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    x = 1000
    for i in range(x):
        job = multiprocessing.Process(target=Test.worker, args=(i, return_dict))
        jobs.append(job)
        job.start()

    for job in jobs:
        job.join()

    print return_dict
