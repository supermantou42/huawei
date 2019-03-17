import logging
import sys
import Entity

logging.basicConfig(level=logging.DEBUG,
                    filename='../../logs/CodeCraft-2019.log',
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')


def main():
    if len(sys.argv) != 5:
        logging.info('please input args: car_path, road_path, cross_path, answerPath')
        exit(1)

    car_path = sys.argv[1]
    road_path = sys.argv[2]
    cross_path = sys.argv[3]
    answer_path = sys.argv[4]

    logging.info("car_path is %s" % (car_path))
    logging.info("road_path is %s" % (road_path))
    logging.info("cross_path is %s" % (cross_path))
    logging.info("answer_path is %s" % (answer_path))

    for i in range(10):
        car_list, cross_list, road_list = Entity.read('config_%d' % (i + 1))
        my_map = Entity.Map(road_list, cross_list, car_list)
        my_map.plot()

    # print(len(car_list))
    # print(len(cross_list))
    # print(len(road_list))


# to read input file
# process
# to write output file


if __name__ == "__main__":
    main()
