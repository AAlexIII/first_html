import subprocess
import argparse
import time


def give_time(f):

    def d(arg1, arg2):
        start_time = time.time()
        r = f(arg1, arg2)
        print("--- %s seconds ---" % (time.time() - start_time))
        return r
    return d

def print_hi(name):
    reply = subprocess.run('ping -n 2 195.201.201.32 195.201.201.32')
    print(reply)
    print(reply.args)
    print(reply.check_returncode)
    print(reply.returncode)
    print(dir(reply))


@give_time
def ping_ip(ip_address, count):
    """
    Ping IP address and return tuple:
    On success: (return code = 0, command output)
    On failure: (return code, error output (stderr))
    """
    reply = subprocess.run('ping -n {count} {ip}'
                           .format(count=count, ip=ip_address),
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='cp866')
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stdout + reply.stderr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ping script')

    parser.add_argument('-a', action="store", dest="ip", )
    parser.add_argument('-c', action="store", dest="count", default=2, type=int)

    args = parser.parse_args()
    #print(args)

    # rc, message = ping_ip(args.ip, args.count)

    ping_ip("8.8.8.8", 1)
    #print(message)rc, message = ping_ip("8.8.8.8", 2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
