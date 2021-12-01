import numpy as np


class RecursiveConnectedComponentLabeler:

    def search(self, label_img, label, i, j):
        max_rows, max_cols = int(label_img.shape[0]), int(label_img.shape[1])

        if i < 0 or i >= max_rows:
            return
        if j < 0 or j >= max_cols:
            return

        label_img[i, j] = label
        neighborhood = label_img[i-1:i+2, j-1:j+2]
        for n in range(neighborhood.shape[0]):
            for m in range(neighborhood.shape[1]):
                if neighborhood[n, m] == -1:
                    self.search(label_img, label, i + n - 1, j + m - 1)

    def find_components(self, label_img, label):
        max_rows, max_cols = label_img.shape[0], label_img.shape[1]

        for i in range(max_rows):
            for j in range(max_cols):
                if label_img[i, j] == -1:
                    label = label + 1
                    self.search(label_img, label, i, j)
                    f = open(f"steps/{label}.txt", "w")
                    for ii in range(max_rows):
                        for jj in range(max_cols):
                            f.write(str(int(label_img[ii, jj]) + 1))
                            if jj < (max_cols-1):
                                f.write(", ")
                        f.write("\n")
                    f.close()

    def label_components(self, binary_img):
        label_img = -binary_img
        label = 0
        self.find_components(label_img, label)
        return label_img


class RecursiveConnectedComponentLabeler2:
    def neighbor(self, i, j, label):
        left = label[i-1, j]
        above = label[i, j-1]
        neighbor_array = [left, above]
        return neighbor_array

    def label_components(self, gray):
        size = gray.shape  
        m = size[0]  # rows
        n = size[1]  # columns

        gray = gray

        label = np.ones([m, n])
        new = 0

        link = []
        id = 0

        for row in range(m):
            for column in range(n):
                if gray[row,column] == [0] :
                    label[row, column] = 0
                else :
                    current_neighbor = self.neighbor(row,column,label)

                    if current_neighbor == [0,0]:
                        new= new + 1
                        label[row, column] = new
                    else :
                        if np.min(current_neighbor) == 0 or current_neighbor[0] == current_neighbor[1] :
                            label[row,column] = np.max(current_neighbor)
                        else:
                            label[row,column] = np.min(current_neighbor)
                            if id == 0:
                                link.append(current_neighbor)
                                id = id +1
                            else:
                                check = 0
                                for k in range(id) :
                                    tmp = set(link[k]).intersection(set(current_neighbor))
                                    if len(tmp) != 0 :
                                        link[k] = set(link[k]).union(current_neighbor)
                                        np.array(link)
                                        check = check + 1
                                if check == 0:
                                    id = id + 1
                                    np.array(link)
                                    link.append(set(current_neighbor))

        first_pass_result = label * 1

        for row in range(m):
            for column in range(n):
                for x in range(id):
                    if (label[row, column] in link[x]) and label[row, column] !=0 :
                        label[row, column] = min(link[x])

        second_pass_result = label * 1

        for row in range(m):
            for column in range(n):
                for x in range(id):
                    if (label[row, column] == min(link[x])):
                        label[row, column] = x+1
        return first_pass_result, second_pass_result, label

