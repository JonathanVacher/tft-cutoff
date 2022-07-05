
'''
GNU General Public License v3.0
Jonathan Vacher, 07/2022
'''
from numpy import arange, zeros, tile, indices, newaxis
from numpy import sort, unique, histogram, int32, fromstring
from numpy.random import default_rng
from matplotlib.pyplot import subplots, show, axes
from matplotlib.widgets import Button, TextBox
import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None' 

if __name__=='__main__':
    
    # set up the figure
    fig, ax  = subplots(1,1, figsize=(7,8))
    fig.text(0.91,0.01,'by BiToP', fontsize=10)
    fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)
    fig.canvas.manager.set_window_title('TFT Cutoff Calculator')
 
    def run_simulation(N_joueurs, N_cutoff, N_game, points):
        '''
        This function update the figure where the histogram of the number of 
        points of the player at the cutoff is plotted.  

        Parameters
        ----------
        N_joueurs : int 
            Number of players in a game.
        N_cutoff : int
            Rank of the last qualified player for the rest of the 
            tournament.
        N_game : int
            Number of games to qualify for the rest of the 
            tournament.
        points : str of comma separated numbers
            Points attribution to each player in a game.


        Returns
        -------
        None : running the function update the figure.

        '''

        # internal parameters
        N_sample = 10000
        joueurs_par_game = 8
        N_lobby = N_joueurs//joueurs_par_game
        joueur_id = arange(N_joueurs)
        point_joueurs = zeros((N_sample,N_game,N_joueurs))

        # simulation of games outcome for all players
        rng = default_rng()
        lobby = rng.permuted(tile(joueur_id[newaxis,newaxis],
                                    (N_sample,N_game,1)), axis=2)
        chan, row, _ = indices((N_sample,N_game,N_joueurs))
        point_joueurs[chan,row,lobby] = tile(points,(N_sample,N_game,N_lobby))

        # get the number of point of the last player before cutoff
        cut_off_point = sort(point_joueurs.sum(1))[:,::-1][:,N_cutoff-1]

        # average and standard devition
        cut_off_point_m = cut_off_point.mean()
        cut_off_point_std = cut_off_point.std()

        # plotting histogram
        points_possible = unique(cut_off_point)
        n_bins = points_possible.shape[0]
        count, _ = histogram(cut_off_point, bins=n_bins)
        points_possible = unique(cut_off_point)
        freq = 100*count/count.sum()
       
        ax.bar(points_possible,freq)
        ax.text(0.05,0.9,'ave. : %.2f pts'%(cut_off_point_m),
                transform=ax.transAxes, fontsize=18)
        ax.text(0.55,0.9,'std : %.2f pts'%(cut_off_point_std),
                transform=ax.transAxes, fontsize=18)
        ax.set_ylim(0, 1.25*freq.max())
        ax.set_xticks(points_possible)
        ax.tick_params(labelsize=16)
        ax.set_xlabel('points',fontsize=18)
        ax.set_ylabel('proportion (%)',fontsize=18, labelpad =10)
        
    # define 'run' button
    run_ax = axes([0.85, 0.92, 0.1, 0.04])
    button = Button(run_ax, 'Run', color='white', hovercolor='0.975')

    # default params ('initial')
    # define input fields
    N_joueurs_ax = axes([0.3, 0.94, 0.1, 0.04])
    N_joueurs_field = TextBox(N_joueurs_ax, 'Nbr de joueurs: ', initial=32)

    N_cutoff_ax = axes([0.6, 0.94, 0.1, 0.04])
    N_cutoff_field = TextBox(N_cutoff_ax, 'Cutoff: ', initial=8)

    N_game_ax = axes([0.3, 0.89, 0.1, 0.04])
    N_game_field = TextBox(N_game_ax, 'Nbr de game: ', initial=5)

    points_ax = axes([0.6, 0.89, 0.2, 0.04])
    points_field = TextBox(points_ax, 'Attrib des pts: ', 
                    initial='1,2,3,4,5,6,7,8')

    def run(event):
        ''' 
        This function is run when the user clicks the button 'run'
        '''
        ax.cla()
        run_simulation(int32(N_joueurs_field.text), 
                       int32(N_cutoff_field.text),
                       int32(N_game_field.text),
                       fromstring(points_field.text,dtype=int, sep=','))
        fig.canvas.draw()

    button.on_clicked(run)
    show()

    


