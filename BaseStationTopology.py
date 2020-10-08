import numpy as np
import matplotlib.pyplot as plt
"""This algorithm provides a solution for generating base station topology in a cellular network. 
The following codes simulate 3-tier cellular scenario, in which we get 6 + 12 + 18 + 1 = 37 locations of base stations.
A 2-tier or 1-tier topology can be generated via simply modifying the following codes. 
In the cases of 1-tier, we get 6 + 1 = 7 base stations in total, and we get 6 + 12 + 1 = 19 base stations for 2-tier scenario.
"""
class TerrestrialCellular(object):
	def __init__(self, n_bs=None, n_gue=None, cell_radius=200):
		self.n_bs = n_bs
		self.n_gue = n_gue
		self.cell_radius = cell_radius # the half distance between 2 neighbouring base stations
		self.bs_list = []

	def gen_bs_list(self):
		r = self.cell_radius
		bs_locations = [[0, 0]] # the origin base station, around which there are 1-st tier cells, 2-nd tier cells, 3-rd tier cells, and so on.
		theta_1 = 2 * np.pi / 6 * np.arange(0, 6) 
		theta_2 = 2 * np.pi / 6 * np.arange(0, 6) - np.pi / 6 
		theta_3 = 2 * np.pi / 6 * np.arange(0, 6) - np.pi / 6 - np.pi / 9 
		theta_4 = 2 * np.pi / 6 * np.arange(0, 6) - np.pi / 6 - np.pi / 9 - np.pi / 9  
		r1 = 2 * r  # 1-st tier, 6 base stations in total
		r21 = 4 * r  # 2-nd tier, 12 base stations in total, r21 represents the first 6 stations
		r22 = 4 * r / 2 * np.sqrt(3)  # 2-nd tier, 12 base stations in total, r22 represents the second 6 stations
		r31 = 6 * r  # 3-rd tier, 18 base stations in total, r31 represents the first 6 stations
		r32 = np.sqrt(28) * r  # 3-rd tier, 18 base stations in total, r32 represents the second 6 + 6 = 12 stations

		positions = r22 * np.vstack((np.cos(theta_1), np.sin(theta_1))).transpose()
		positions = positions.tolist()
		bs_locations += positions

		positions = r1 * np.vstack((np.cos(theta_2), np.sin(theta_2))).transpose()  # e.g., np.vstack((1, 2)).transpose() = array([[1, 2]]) and np.vstack((1, 2)).transpose().tolist() = [[1, 2]]
		positions = positions.tolist()  # convert numpy array to list
		bs_locations += positions  # e.g., [[1, 2]] + [[3, 4]] = [[1, 2], [3, 4]] and the shape is 2*2
		positions = r21 * np.vstack((np.cos(theta_2), np.sin(theta_2))).transpose()
		positions = positions.tolist()
		bs_locations += positions
		positions = r31 * np.vstack((np.cos(theta_2), np.sin(theta_2))).transpose()
		positions = positions.tolist()
		bs_locations += positions

		positions = r32 * np.vstack((np.cos(theta_3), np.sin(theta_3))).transpose()
		positions = positions.tolist()
		bs_locations += positions
		positions = r32 * np.vstack((np.cos(theta_4), np.sin(theta_4))).transpose()
		positions = positions.tolist()
		bs_locations += positions

		bs_locations = np.array(bs_locations)
		for index in range(bs_locations.shape[0]):
			self.bs_list.append(bs_locations[index, :])

	def show_topo(self):
		x, y = [], []
		for bs in self.bs_list:
			x.append(bs[0])
			y.append(bs[1])

		plt.figure(figsize=(10, 10))
		plt.scatter(x, y, marker='o', c='red', s=50, edgecolor=None, label='Base Station')
		plt.show()

if __name__ == '__main__':
	a = TerrestrialCellular()
	b = a.gen_bs_list()
	c = a.show_topo()
