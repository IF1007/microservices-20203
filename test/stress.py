import requests
import time


URL_TEASTORE = 'http://localhost:8080/tools.descartes.teastore.webui/'
URL_CATEGORY = 'http://localhost:8080/tools.descartes.teastore.webui/category?category=*&page=1'
URL_ORDER = 'http://localhost:8080/tools.descartes.teastore.webui/order'


class Stress(object):
    def __init__(self):
        self.log = '[LOG - Stress]'

    def basic_stress(self, attempt=35):
        """
        Send requests n times to test the application
        :param attempt: Number of attempt. Default = 35
        :return:
        """
        i = 0
        print('{} - Starting basic test stress'.format(self.log))
        for _ in range(1, attempt):
            print('Running {} of {}'.format(i, attempt))
            r = requests.get(URL_TEASTORE)
            i += 1
            assert r.status_code == requests.codes.ok, '{} - On attempt {} fail to GET request'.format(self.log, i)
            time.sleep(30)
        return True

    def category_stress(self, attempt=35):
        """
        Send requests n times to test the category application
        :param attempt: Number of attempt. Default = 35
        :return:
        """
        i = 0
        print('{} - Starting category test stress'.format(self.log))
        for _ in range(1, attempt):
            print('Running {} of {}'.format(i, attempt))
            for category_index in range(2, 7):
                print('{} - Running category {} of {}'.format(self.log, category_index, 6))  # Todo fix the number log
                r = requests.get(URL_CATEGORY.replace("*", str(category_index)))
                print(URL_CATEGORY.replace("*", str(category_index)))
                assert r.status_code == requests.codes.ok, '{} - On attempt {} fail to request category {}'.format(
                    self.log, i, category_index)
                time.sleep(30)
            i += 1
        return True

    def post_basic_stress(self, attempt=35):
        """
        Send requests n times to test the application order
        :param attempt: Number of attempt. Default = 35
        :return:
        """
        i = 0
        print('{} - Starting basic test stress'.format(self.log))
        for _ in range(1, attempt):
            print('Running {} of {}'.format(i, attempt))
            r = requests.post(URL_ORDER)
            i += 1
            assert r.status_code == requests.codes.ok, '{} - On attempt {} fail to POST request'.format(self.log, i)
            time.sleep(30)
        return True


if __name__ == '__main__':
    test_stress = Stress()
    test_stress.category_stress()
