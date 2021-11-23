from sources.markov import MarkovDecisionProcess
from sources.world import World
from argparse import ArgumentParser
from time import time

if __name__ == "__main__":
    parser = ArgumentParser(description='Implementation of Markov Decision Problem'
                                                 'using GridWorld environment. Use -h for more informations.')
    parser.add_argument('world_filename', help="Chosen world filename. Eg. \"world1.txt\"")
    parser.add_argument('-mdp', '--mrun', action="store_true", help="Run Markov Decision Problem algorithm")
    parser.add_argument('-sh', '--show', action="store_true", help="Show figures")
    parser.add_argument('-s', '--save', action="store_true", help="Save figures and data to tmp.*"
                                                                  " To change filename use: -sfn [filename]")
    parser.add_argument('-sfn', '--save_filename', help="Change saved figures file names. Use -sfn [filename]"
                                                        " (DO NOT USE FILE EXTENSION!)", default="tmp", required=False)
    args = parser.parse_args()

    print("*********** PARSER INFO **************")
    print("World filename: ", args.world_filename)
    print("Run MDP: ", args.mrun)
    print("Show figures: ", args.show)
    print("Save figures: ", args.save)
    print("Figures filename: ", args.save_filename)
    print("***************************************")


    if args.mrun is False:
        print("ERROR: At least [-mdp] option have to be use to execute this program!")
    else:
        world = World()
        world.readFile(str(args.world_filename))
        world.showWorldValues()

        if args.mrun:
            markov = MarkovDecisionProcess(world)
            print("\n\n ## Markov Decision Process ##")
            start_time = time()
            utilities, policy, iter = markov.value_iteration()
            elapsed_time = time() - start_time
            print("Number of iteration: ", iter)
            print("Algorithm execution time: ", round(elapsed_time, 2), " s")
            print("\n ++ Utilities and Policy ++")
            world.plotUtilitiesActionText(utilities, policy)
            if args.show is True and args.save is False:
                util_plot = world.plotUtilities(utilities, "mdp")
                policy_plot = world.plotPolicy(policy, "mdp")
                policy_plot.show()

            if args.save is True:
                util_plot = world.plotUtilities(utilities, "mdp")
                world.saveUtilitiesPlot(util_plot, str(args.save_filename), "mdp")
                policy_plot = world.plotPolicy(policy, "mdp")
                world.savePolicyPlot(policy_plot, str(args.save_filename), "mdp")
                if args.show is True:
                    policy_plot.show()
