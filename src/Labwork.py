from Image import Image


class LabTest:
    """
    <<interface>>
    """

    def make_request(self):
        pass

    def get_request(self):
        pass

    def enter_result(self):
        pass

    def get_result(self):
        pass


class LabRequest:
    """
    <<interface>>
    """

    def set_request(self, details):
        pass

    def get_request(self):
        pass


class LabResult:
    """
    <<interface>>
    """

    def set_result(self, result):
        pass

    def get_result(self):
        pass


class BloodWorkRequest(LabRequest):
    def __int__(self, sender, recipient, patient_ID, details):
        """

        :param sender:
        :param recipient:
        :param patient_ID:
        :param details:
        :return:
        """
        self.requested_by = sender
        self.sent_to = recipient
        self.patient_ID = patient_ID
        self.details = details

    def set_request(self, details):
        """

        :param details:
        :return:
        """
        self.details = details

    def get_request(self):
        """

        :return: Information on the request as a string.
        """
        request = "sent by: " + self.requested_by + ", " \
                  + "sent to: " + self.sent_to \
                  + ", patient ID: " + str(self.patient_ID) \
                  + ", details: " + self.details
        return request


class ImagingRequest(LabRequest):
    def __init__(self, sender, recipient, patient_ID, details):
        """

        :param sender:
        :param recipient:
        :param patient_ID:
        :param details:
        :return:
        """
        self.requested_by = sender
        self.sent_to = recipient
        self.patient_ID = patient_ID
        self.details = details

    def set_request(self, details):
        """

        :param details:
        :return:
        """
        self.details = details

    def get_request(self):
        """

        :return: Information on the request as a string.
        """
        request = "sent by: " + self.requested_by + ", " \
                  + "sent to: " + self.sent_to \
                  + ", patient ID: " + str(self.patient_ID) \
                  + ", details: " + self.details
        return request


class BloodworkResult:
    def __int__(self):
        """

        :return:
        """
        self.result = ""

    def __init__(self, result):
        """

        :param result:
        """
        self.result = result

    def set_result(self, result):
        self.result = result

    def get_result(self):
        return self.result


class ImagingResult(LabResult):
    def __int__(self):
        """

        :return:
        """
        self.images_taken = []

    def __init__(self, images):
        """

        :param images:
        """
        self.images_taken = images

    def set_result(self, images):
        self.images_taken = images

    def get_result(self):
        return self.images_taken


class BloodTest(LabTest):
    pass


class ImagingTest(LabTest):
    pass
