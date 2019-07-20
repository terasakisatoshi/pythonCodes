import random
import statistics

box_a = ['r', 'b']
box_b = ['r', 'b', 'b', 'b']
box_c = ['r', 'r', 'b', 'b', 'b']
box_set = [box_a, box_b, box_c]
box_index = list(range(len(box_set)))


def choice_balls():
    idx_choiced = random.choice(box_index)
    box_choiced = box_set[idx_choiced]
    balls = random.sample(box_choiced, 2)
    return balls

def try_pickup(trial=100,num_condi=1):
    counter = 0
    for i in range(trial):
        balls = choice_balls()
        bs=sum(ball=='b' for ball in balls)
        if bs == num_condi:
            counter+=1
    return 1.0*counter/trial

def main():
    probs_0=[try_pickup(num_condi=0) for _ in range(1000)]
    probs_1=[try_pickup(num_condi=1) for _ in range(1000)]
    probs_2=[try_pickup(num_condi=2) for _ in range(1000)]
    mean_0=statistics.mean(probs_0)
    mean_1=statistics.mean(probs_1)
    mean_2=statistics.mean(probs_2)
    print(mean_0,mean_1,mean_2)
    print('check sum',mean_0+mean_1+mean_2)


if __name__ == '__main__':
    main()
