import requests
import time
import argparse

URL_TEASTORE = 'http://localhost:8080/tools.descartes.teastore.webui/'
URL_CATEGORY = 'http://localhost:8080/tools.descartes.teastore.webui/category?category=*&page=1'
URL_ORDER = 'http://localhost:8080/tools.descartes.teastore.webui/order'


class Stress(object):
    def __init__(self):
        self.log = '[LOG - Stress]'

    def get_basic_stress(self, attempt=35, freq_request=30, timeout=0.01):
        """
        Send requests n times to test the application
        :param attempt: Number of attempt. Default = 35
        :param freq_request: Freq of request
        :param timeout: The timeout of each request
        :return:
        """
        i = 0
        print('{} - Starting basic test stress'.format(self.log))
        for _ in range(1, attempt):
            print('Running {} of {}'.format(i, attempt))
            r = requests.get(URL_TEASTORE, timeout=timeout)
            i += 1
            assert r.status_code == requests.codes.ok, '{} - On attempt {} fail to GET request'.format(self.log, i)
            time.sleep(freq_request)
        return True

    def post_basic_stress(self, attempt=35, freq_request=30):
        """
        Send requests n times to test the application order
        :param attempt: Number of attempt. Default = 35
        :param freq_request: Freq of request
        :return:
        """
        i = 0
        print('{} - Starting basic test stress'.format(self.log))
        for _ in range(1, attempt):
            print('Running {} of {}'.format(i, attempt))
            r = requests.post(URL_ORDER)
            i += 1
            assert r.status_code == requests.codes.ok, '{} - On attempt {} fail to POST request'.format(self.log, i)
            time.sleep(freq_request)
        return True

    def category_stress(self, attempt=35, freq_request=30, timeout=0.01):
        """
        Send requests n times to test the category application
        :param attempt: Number of attempt. Default = 35
        :param freq_request: Freq of request
        :param timeout: The timeout of each request
        :return:
        """
        i = 0
        print('{} - Starting category test stress'.format(self.log))
        for _ in range(1, attempt):
            print('Running {} of {}'.format(i, attempt))
            for category_index in range(2, 7):
                print('{} - Running category {} of {}'.format(self.log, category_index, 6))  # Todo fix the number log
                r = requests.get(URL_CATEGORY.replace("*", str(category_index)), timeout=timeout)
                print(URL_CATEGORY.replace("*", str(category_index)))
                assert r.status_code == requests.codes.ok, '{} - On attempt {} fail to request category {}'.format(
                    self.log, i, category_index)
                time.sleep(freq_request)
            i += 1
        return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--freqtime', help='Frequence time on stress test. In seconds')
    parser.add_argument('-tt', '--timeout', help='The timeout from GET request')
    parser.add_argument('-att', '--attempt', help='numbers of attempt on stress test')
    args = parser.parse_args()
    s = Stress()
    s.get_basic_stress(attempt=int(args.attempt), freq_request=int(args.freqtime), timeout=float(args.timeout))
    s.category_stress(attempt=int(args.attempt), freq_request=int(args.freqtime), timeout=float(args.timeout))
    s.post_basic_stress(attempt=int(args.attempt), freq_request=int(args.freqtime))


if __name__ == '__main__':
    main()
