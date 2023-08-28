from argparse import ArgumentParser
import numpy as np
from signaling_game import SignalingGame
from agents import Sender, Receiver

def get_args():
  parser = ArgumentParser()
  parser.add_argument("num_states", type=int, help="number of states")
  parser.add_argument("num_signals", type=int, help="number of signals")
  parser.add_argument("num_actions", type=int, help="number of actions")
  parser.add_argument("reward_param_1", type=float, 
                      help="first parameter for reward function")
  parser.add_argument("reward_param_2", type=float, 
                      help="second parameter for reward function")
  parser.add_argument("-n", "--null", help="null signal", action="store_true")
  parser.add_argument("num_iter", type=int, 
                      help="number of iterations for simulation")
  parser.add_argument("-r", "--record", type=int, default=-1, help="record interval")

  args = parser.parse_args()

  return (args.num_states, args.num_signals, args.num_actions, 
          args.reward_param_1, args.reward_param_2, args.null,
          args.num_iter, args.record)

def main():
  (nstates, nsignals, nactions, rp1, rp2, null, niter, record) = get_args()

  network_size = 5 # to update

  senders = [Sender(nstates, nsignals, null) for _ in range(network_size)]
  receivers = [Receiver(nsignals, nactions) for _ in range(network_size)]

  game = SignalingGame(nstates, nsignals, nactions, 
                       (rp1, rp2), null_signal=null)

  for iter in range(niter):
    random_senders = np.random.permutation(senders)
    random_receivers = np.random.permutation(receivers)

    for i in range(5):
      if record > 0 and (iter+1) % record == 0:
        game(random_senders[i], random_receivers[i], 1, 1)
      else:
        game(random_senders[i], random_receivers[i], 1)

if __name__ == '__main__':
  main()