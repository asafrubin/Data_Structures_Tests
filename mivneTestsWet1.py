import random
import numpy

class Image:
    def __init__(self, imageID, numOfSegments):
        self.imageID = imageID
        self.numOfSegments = numOfSegments
        self.segments = {}

    def add_label(self, segmentID, labelID):
        self.segments[segmentID] = labelID
        return None

    def get_segment_label(self, segmentID):
        return self.segments.get(segmentID, 0)

    def set_segment_label(self, segment_id, label_id):
        self.segments[segment_id] = label_id
        return None

    def remove_label(self, segment_id):
        del self.segments[segment_id]
        return None

    def isFullyLabeled(self):
        check12 = len(self.segments)
        return len(self.segments) == segment_init

    def getAllUnLabeled(self):
        unlabeled = []
        for i in range(0, self.numOfSegments):
            if self.segments.get(i, 0) == 0:
                unlabeled.append(i)
            else:
                continue
        return unlabeled
images = {}

max_image_id = 1000
min_image_id = -1

max_segment_id = 20
min_segment_id = -1

max_label_id = 25
min_label_id = -1


def addImage():
    image_id = random.randint(min_image_id, max_segment_id)
    test_in.write("addImage {0}\n".format(image_id))
    if image_id <= 0 :
        test_out.write("addImage: INVALID_INPUT\n")
    elif images.get(image_id, 0) != 0:
        test_out.write("addImage: FAILURE\n")
    else:
        images[image_id] = Image(image_id, segment_init)
        test_out.write("addImage: SUCCESS\n")
        tree_test_out.write("add image in line {0} : ".format(x+2))
        for image in sorted(images):
            tree_test_out.write("{0} ".format(image))
            tree_test_out_clear.write("{0} ".format(image))
        tree_test_out.write("\n")
        tree_test_out_clear.write("\n")
        #print(images)
    return None

def deleteImage():
    image_id = random.randint(min_image_id, max_segment_id)
    test_in.write("deleteImage {0}\n".format(image_id))
    if image_id <= 0:
        test_out.write("deleteImage: INVALID_INPUT\n")
    elif images.get(image_id, 0) == 0:
        test_out.write("deleteImage: FAILURE\n")
    else:
        del images[image_id]
        test_out.write("deleteImage: SUCCESS\n")
        tree_test_out.write("delete image in line {0} : ".format(x+2))
        for image in sorted(images):
            tree_test_out.write("{0} ".format(image))
            tree_test_out_clear.write("{0} ".format(image))
        tree_test_out.write("\n")
        tree_test_out_clear.write("\n")
    return None

def addLabel():
    image_id = random.randint(min_image_id, max_segment_id)
    segment_id = random.randint(min_segment_id, max_segment_id)
    label_id = random.randint(min_label_id, max_label_id)
    test_in.write("addLabel {0} {1} {2}\n".format(image_id, segment_id, label_id))
    if image_id <= 0 or segment_id < 0 or segment_id >= segment_init or label_id <= 0:
        test_out.write("addLabel: INVALID_INPUT\n")
    elif images.get(image_id, 0) == 0 or Image.get_segment_label(images[image_id], segment_id) != 0:
        test_out.write("addLabel: FAILURE\n")
    else:
        Image.set_segment_label(images[image_id], segment_id, label_id)
        test_out.write("addLabel: SUCCESS\n")
    return None

def getLabel():
    image_id = random.randint(min_image_id, max_segment_id)
    segment_id = random.randint(min_segment_id, max_segment_id)
    test_in.write("getLabel {0} {1}\n".format(image_id, segment_id))
    if image_id <= 0 or segment_id < 0 or segment_id >= segment_init:
        test_out.write("getLabel: INVALID_INPUT\n")
    elif images.get(image_id, 0) == 0 or Image.get_segment_label(images[image_id], segment_id) == 0:
        test_out.write("getLabel: FAILURE\n")
    else:
        label_id = Image.get_segment_label(images[image_id], segment_id)
        test_out.write("getLabel: {0}\n".format(label_id))
    return None

def deleteLabel():
    image_id = random.randint(min_image_id, max_segment_id)
    segment_id = random.randint(min_segment_id, max_segment_id)
    test_in.write("deleteLabel {0} {1}\n".format(image_id, segment_id))
    if image_id <= 0 or segment_id < 0 or segment_id >= segment_init:
        test_out.write("deleteLabel: INVALID_INPUT\n")
    elif images.get(image_id, 0) == 0 or Image.get_segment_label(images[image_id], segment_id) == 0:
        test_out.write("deleteLabel: FAILURE\n")
    else:
        Image.remove_label(images[image_id], segment_id)
        test_out.write("deleteLabel: SUCCESS\n")
    return None

def getAllUnLabeledSegments():
    image_id = random.randint(min_image_id, max_segment_id)
    abcs = images.get(image_id, 0)
    test_in.write("getAllUnLabeledSegments {0}\n".format(image_id))
    if image_id <= 0:
        test_out.write("getAllUnLabeledSegments: INVALID_INPUT\n")
    elif images.get(image_id, 0) == 0 or Image.isFullyLabeled(images.get(image_id)):
        test_out.write("getAllUnLabeledSegments: FAILURE\n")
    else:
        to_print = Image.getAllUnLabeled(images.get(image_id))
        test_out.write("getAllUnLabeledSegments: SUCCESS\n")
        for x in to_print:
            test_out.write(str(x) + "\n")
        test_out.write("--End of segments list--\n")
    return None

def getAllSegmentsByLabel():
    label_id = random.randint(min_label_id, max_label_id)
    test_in.write("getAllSegmentsByLabel {0}\n".format(label_id))
    if label_id <= 0:
        test_out.write("getAllSegmentsByLabel: INVALID_INPUT\n")
    else:
        labeled_list = []
        for image in images.itervalues():
            for segmentID in range(0, segment_init):
                if Image.get_segment_label(image, segmentID) == label_id:
                    labeled_list.append((image.imageID, segmentID))
                else:
                    continue
        test_out.write("getAllSegmentsByLabel: SUCCESS\n")
        a = len(labeled_list)
        if len(labeled_list) > 0:
            labeled_list.sort(key=lambda tup: tup[0])
            test_out.write("Image	||	Segment\n")
            for item in labeled_list:
                test_out.write(str(item[0]) +  "	||	" + str(item[1]) + "\n")
        test_out.write("--End of segments list--\n")
    return None

def getAllSegmentsByLabel_2(label_id):
    #label_id = random.randint(min_label_id, max_label_id)
    test_in.write("getAllSegmentsByLabel {0}\n".format(label_id))
    if label_id <= 0:
        test_out.write("getAllSegmentsByLabel: INVALID_INPUT\n")
    else:
        labeled_list = []
        for image in images.itervalues():
            for segmentID in range(0, segment_init):
                if Image.get_segment_label(image, segmentID) == label_id:
                    labeled_list.append((image.imageID, segmentID))
                else:
                    continue
        test_out.write("getAllSegmentsByLabel: SUCCESS\n")
        a = len(labeled_list)
        if len(labeled_list) > 0:
            labeled_list.sort(key=lambda tup: tup[0])
            test_out.write("Image	||	Segment\n")
            for item in labeled_list:
                test_out.write(str(item[0]) + "	||	" + str(item[1]) + "\n")
        test_out.write("--End of segments list--\n")
    return None

lines = 50000

for number in range(200, 201):
    test_in = open("randTest{0}.in".format(number), "w")
    test_out = open("randTest{0}.out".format(number), "w")
    tree_test_out = open("treeTest{0}.out".format(number), "w")
    tree_test_out_clear = open("treeTestClear{0}.out".format(number), "w")

    segment_init = random.choice(list(range(1, max_segment_id)))
    test_in.write("init " + str(segment_init) + "\n")
    test_out.write("init done.\n")
    funcs = [addImage, deleteImage, addLabel, getLabel, deleteLabel, getAllUnLabeledSegments, getAllSegmentsByLabel]
    range_ = list(range(0,len(funcs)))
    for x in range(lines):
        index = numpy.random.choice(range_, p=[0.4, 0.01, 0.3, 0.01, 0.05, 0.05, 0.18])
        funcs[index]()
    for label_id in range(min_label_id, max_label_id):
        getAllSegmentsByLabel_2(label_id)
    test_in.write("quit\n")
    test_out.write("quit done.\n")
    test_in.close()
    test_out.close()
    tree_test_out.close()
    images.clear()
