import logging
import sys
import Entity
import numpy as np
np.set_printoptions(threshold=np.inf)


logging.basicConfig(level=logging.DEBUG,
#C:\Users\yixu\Desktop\软件挑战赛\huawei\logs
                    filename='C:/Users/yixu/Desktop/软件挑战赛/huawei/logs/CodeCraft-2019.log',
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')


def main():

 #   if len(sys.argv) != 5:
#        logging.info('please input args: car_path, road_path, cross_path, answerPath')
  #      exit(1)

  #  car_path = sys.argv[1]
  #  road_path = sys.argv[2]
 #   cross_path = sys.argv[3]
  #  answer_path = sys.argv[4]

 #   logging.info("car_path is %s" % (car_path))
 #   logging.info("road_path is %s" % (road_path))
  #  logging.info("cross_path is %s" % (cross_path))
  #  logging.info("answer_path is %s" % (answer_path))


    carlist, crosslist, roadlist = Entity.read('config_10')
    Min_way=Entity.Min_way(roadlist)
    zz=Min_way.getminway()
    print(Min_way.returnvisitpath(1,36))
    for i in range(9,11):
        print(i)
        print(zz[i])




    map = Entity.Map(roadlist, crosslist, carlist)
    map.plot()

    print(len(carlist))
    print(len(crosslist))
    print(len(roadlist))


# to read input file
# process
# to write output file


if __name__ == "__main__":
    main()
