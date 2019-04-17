import random
import numpy


class Label:
    def __init__(self, label_id, label_score):
        self.id = label_id
        self.score = label_score

class Pixel:
    def __init__(self, pixel_id):
        self.group_id = pixel_id
        self.id = pixel_id
        self.group_size = 1
        self.labels = {}

    def set_label_score(self, label):
        if self == 0:
            return
        self.labels[label.id] = label.score

    def reset_label(self, label):
        del self.labels[label]

    def get_pixel_group(self):
        if self == 0 :
            return -1
        return self.group_id

    def set_group(self, group_id):
        self.group_id = group_id

    def check_if_labels_empty(self):
        if(self == 0):
            return True
        else:
            return len(self.labels) == 0

    def merge(self, pixel):
        pixel_labels = getattr(pixel, 'labels')
        #intersections.write("left side: {0}\n".format(list(self.labels.items())))
        #intersections.write("right side: {0}\n".format(list(pixel_labels.items())))
        inter = self.labels.keys() & pixel_labels.keys()
        #intersections.write("intersection keys: {0}\n".format(list(inter)))
        for x in inter:
            self.labels[x] = self.labels[x] + pixel_labels[x]
            del pixel_labels[x]
        #intersections.write("before union: {0}\n".format(self.labels.items()))
        self.labels = { **self.labels, **pixel_labels}
        #intersections.write("after union: {0}\n".format(self.labels.items()))
        self.group_size += pixel.group_size
        old_group_id = pixel.get_pixel_group()
        Pixel.set_group(pixel, self.group_id)
        pixel_labels.clear()
        return (old_group_id, self.group_id)

class Image:
    def __init__(self, imageID, numOfPixels):
        self.imageID = imageID
        self.numOfPixels = numOfPixels
        self.pixels = {}
        for pixel in range(0, pixel_init):
            self.pixels[pixel] = Pixel(pixel)

    def set_label_score(self, pixelID, label, score):
        new_label = Label(label, score)
        pixel = self.get_pixel(pixelID)
        pixel.set_label_score(new_label)
        return None

    def reset_label_score(self, pixelID, label_id):
        pixel = self.get_pixel(pixelID)
        pixel.reset_label(label_id)

    def pixel_label_exists(self, pixelID, label_id):
        pixel = self.get_pixel(pixelID)
        return label_id in pixel.labels

    def getHighestScored(self, pixelID):
        pixel = self.get_pixel(pixelID)
        max_label = Label(0,0)
        for id, score in pixel.labels.items():
            if score > max_label.score:
                max_label = Label(id, score)
            elif score == max_label.score:
                if id > max_label.id:
                    max_label = Label(id, score)
        return max_label

    def mergeSuperPixels(self, pixel_1, pixel_2):
        pixel_to_set_1 = self.get_pixel(pixel_1)
        pixel_to_set_2 = self.get_pixel(pixel_2)

        if getattr(pixel_to_set_1, 'group_size') <= getattr(pixel_to_set_2, 'group_size'):
            (old_group_id, new_group_id) = Pixel.merge(pixel_to_set_2, pixel_to_set_1)
        else:
            (old_group_id, new_group_id) = Pixel.merge(pixel_to_set_1, pixel_to_set_2)
        for x in self.pixels:
            if self.pixels[x].group_id == old_group_id :
                self.pixels[x].group_id = new_group_id
        return None

    def get_pixel(self, pixelID):
        pixel = self.pixels.get(pixelID)
        if pixel.id != pixel.group_id:
            pixel = self.pixels.get(pixel.group_id)
        return pixel

    def in_same_super_pixel(self, pixel_1, pixel_2):
        return self.get_pixel(pixel_1).group_id == self.get_pixel(pixel_2).group_id

    def check_if_labels_empty(self, pixelID):
        return len(self.get_pixel(pixelID).labels) == 0


images = {}

max_image_id = 100
min_image_id = -1

max_pixel_id = 10
min_pixel_id = -1

max_label_id = 10
min_label_id = -1

max_label_score = 100
min_label_score = -1


def addImage():
    image_id = random.randint(min_image_id, max_image_id)
    test_in.write("addImage {0}\n".format(image_id))
    if image_id <= 0 :
        test_out.write("addImage: INVALID_INPUT\n")
    elif images.get(image_id, 0) != 0:
        test_out.write("addImage: FAILURE\n")
    else:
        images[image_id] = Image(image_id, pixel_init)
        test_out.write("addImage: SUCCESS\n")
        #print(images)
    return None

def deleteImage():
    image_id = random.randint(min_image_id, max_image_id)
    test_in.write("deleteImage {0}\n".format(image_id))
    if image_id <= 0:
        test_out.write("deleteImage: INVALID_INPUT\n")
    elif images.get(image_id, 0) == 0:
        test_out.write("deleteImage: FAILURE\n")
    else:
        del images[image_id]
        test_out.write("deleteImage: SUCCESS\n")
    return None


def setLabelScore():
    image_id = random.randint(min_image_id, max_image_id)
    pixel_id = random.randint(min_pixel_id, max_pixel_id)
    label_id = random.randint(min_label_id, max_label_id)
    label_score = random.randint(min_label_score, max_label_score)
    test_in.write("setLabelScore {0} {1} {2} {3}\n".format(image_id, pixel_id, label_id, label_score))
    if image_id <= 0 or pixel_id < 0 or pixel_id >= pixel_init or label_id <= 0 or label_score <= 0:
        test_out.write("setLabelScore: INVALID_INPUT\n")
    elif images.get(image_id, 0) == 0:
        test_out.write("setLabelScore: FAILURE\n")
    else:
        Image.set_label_score(images[image_id], pixel_id, label_id, label_score)
        test_out.write("setLabelScore: SUCCESS\n")
    return None


def resetLabelScore():
    image_id = random.randint(min_image_id, max_image_id)
    pixel_id = random.randint(min_pixel_id, max_pixel_id)
    label_id = random.randint(min_label_id, max_label_id)
    test_in.write("resetLabelScore {0} {1} {2}\n".format(image_id, pixel_id, label_id))
    if image_id <= 0 or pixel_id < 0 or pixel_id >= pixel_init or label_id <= 0:
        test_out.write("resetLabelScore: INVALID_INPUT\n")
    elif images.get(image_id, 0) == 0 or not Image.pixel_label_exists(images[image_id], pixel_id, label_id):
        test_out.write("resetLabelScore: FAILURE\n")
    else:
        Image.reset_label_score(images[image_id], pixel_id, label_id)
        test_out.write("resetLabelScore: SUCCESS\n")
    return None

def getHighestScoredLabel():
    image_id = random.randint(min_image_id, max_image_id)
    pixel_id = random.randint(min_pixel_id, max_pixel_id)
    test_in.write("getHighestScoredLabel {0} {1}\n".format(image_id, pixel_id))
    if image_id <= 0 or pixel_id < 0 or pixel_id >= pixel_init:
        test_out.write("getHighestScoredLabel: INVALID_INPUT\n")
    elif images.get(image_id, 0) == 0 or Image.check_if_labels_empty(images[image_id], pixel_id):
        test_out.write("getHighestScoredLabel: FAILURE\n")
    else:
        label = Image.getHighestScored(images[image_id], pixel_id)
        test_out.write("getHighestScoredLabel: {0}\n".format(label.id))
    return None

def mergeSuperPixels():
    image_id = random.randint(min_image_id, max_image_id)
    pixel_id_1 = random.randint(min_pixel_id, max_pixel_id)
    pixel_id_2 = random.randint(min_pixel_id, max_pixel_id)
    test_in.write("mergeSuperPixels {0} {1} {2}\n".format(image_id, pixel_id_1, pixel_id_2))
    if image_id <= 0 or pixel_id_1 < 0 or pixel_id_1 >= pixel_init or pixel_id_2 < 0 or pixel_id_2 >= pixel_init:
        test_out.write("mergeSuperPixels: INVALID_INPUT\n")
    elif images.get(image_id, 0) == 0 or Image.in_same_super_pixel(images[image_id], pixel_id_1, pixel_id_2):
        test_out.write("mergeSuperPixels: FAILURE\n")
    else:
        Image.mergeSuperPixels(images[image_id], pixel_id_1, pixel_id_2)
        test_out.write("mergeSuperPixels: SUCCESS\n")
    return None


lines = 50000

for number in range(15, 20):
    #lines = setNumOfLines(number)
    test_in = open("randTest{0}.in".format(number), "w")
    test_out = open("randTest{0}.out".format(number), "w")

    pixel_init = random.choice(list(range(1, max_pixel_id)))
    test_in.write("init " + str(pixel_init) + "\n")
    test_out.write("init done.\n")
    funcs = [addImage, deleteImage, setLabelScore, resetLabelScore, getHighestScoredLabel, mergeSuperPixels]
    range_ = list(range(0,len(funcs)))
    for x in range(lines):
        index = numpy.random.choice(range_, p=[0.3, 0.05, 0.2, 0.1, 0.25, 0.1])
        funcs[index]()

    test_in.write("quit\n")
    test_out.write("quit done.\n")
    test_in.close()
    images.clear()