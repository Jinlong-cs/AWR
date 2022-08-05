import numpy as np
import cv2


class Model:
    """ This class contains the NN model(s).
    """
    def __init__(self, checkpoint):
        pass

    def forward(self, img):
        """ Performs forward pass through model. """

        x = 0
        return x


class HandPoseInference:
    """ Hand Pose class to perform pose estimation.
    """
    def __init__(self, model):
        self.model = model
        self.image = 0

    def load_image(self, img):
        self.image = img

    def get_pose_estimation(self):
        """ Calls the model forward path and outputs the pose estimate."""

        wrist_pose = np.zeros(3)

        return wrist_pose


class Visualizer:
    """ Class to visualize pose estimation results.
    """
    # TODO implement visualizer to display pose estimation results results
    def __init__(self):
        self.image = 0
        self.results = 0

    def load_image(self, img):
        self.image = img

    def load_results(self, results):
        self.results = results

    def visualize_results(self):
        pass


def main(img_path, checkpoint_path):

    # Read depth image
    img = cv2.imread(img_path)
    img = np.asarray(img[:, :, 0] + img[:, :, 1] * 256, dtype=np.float32)

    # Setup Model
    model = Model(checkpoint=checkpoint_path)

    # Setup pose estimator
    pose_estimator = HandPoseInference(model=model)
    pose_estimator.load_image(img=img)

    # Setup Visualizer
    pose_visualizer = Visualizer()

    # Get pose
    pose = pose_estimator.get_pose_estimation()
    print(f"Resulting pose :{pose}")
    pose_visualizer.visualize_results()

    return 0


if __name__ == '__main__':

    print("Start Inference")
    # define input
    img_path = "path/to/image"
    checkpoint_path = "path/to/checkpoint"

    main(img_path=img_path, checkpoint_path=checkpoint_path)



