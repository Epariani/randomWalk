import numpy as np
import matplotlib.colors as mcolors
from matplotlib import pyplot as plt
import seaborn as sns


def createIncrements(a):
    increments = np.zeros((len(a), 2))
    increments[:, 0] = np.cos(a)
    increments[:, 1] = np.sin(a)
    return increments


def distances(walk):
    return np.sqrt(np.sum(walk ** 2, axis=1))


def heatmap(walk, levels, facecolor='w', axis_color='k'):
    fig, ax = plt.subplots()
    x = walk[:, 0]
    y = walk[:, 1]
    # sns.scatterplot(x=x, y=y, s=5, color=".15", ax=ax)
    # sns.histplot(x=x, y=y, bins=50, pthresh=.01, cmap="mako", ax=ax)
    sns.kdeplot(x=x, y=y, levels=levels, cmap='terrain', ax=ax,
                fill=True, alpha=1, thresh=0, color='k')
    ax.set_aspect('equal', 'box')
    ax.set_xlim([walk[:, 0].min() - 5, walk[:, 0].max() + 5])
    ax.set_ylim([walk[:, 1].min() - 5, walk[:, 1].max() + 5])
    ax.spines['bottom'].set_color(axis_color)
    ax.spines['top'].set_color(axis_color)
    ax.xaxis.label.set_color(axis_color)
    ax.tick_params(axis='x', colors=axis_color)
    ax.tick_params(axis='y', colors=axis_color)
    fig.patch.set_facecolor(facecolor)
    ax.set_xlim([walk[:, 0].min() - 5, walk[:, 0].max() + 5])
    ax.set_ylim([walk[:, 1].min() - 5, walk[:, 1].max() + 5])
    return fig


class RandomWalk:
    def __init__(self, directions, probs):
        self.directions = directions
        self.angles = np.linspace(0, 2 * np.pi, self.directions, endpoint=False)
        self.increments = createIncrements(self.angles)
        self.probs = probs
        self.dimensions = 2

    def walk(self, x):
        positions = np.cumsum(
            self.increments[np.random.choice(self.directions, size=x, replace=True, p=self.probs)],
            axis=0)
        return np.vstack([np.zeros((1, self.dimensions)), positions])

    def averageDirection(self):
        mean1 = np.sum(self.increments[:, 0] * self.probs, axis=0)
        mean2 = np.sum(self.increments[:, 1] * self.probs, axis=0)
        vector = np.array([mean1, mean2])
        if ~np.isclose(np.linalg.norm(vector), 0):
            return vector / np.linalg.norm(vector)
        return vector

    # Create Plots
    def plot(self, walk, titleFlag, facecolor='w', axis_color='k'):
        fig, ax = plt.subplots()
        ax.plot(walk[:, 0], walk[:, 1], c='black', linewidth=1, zorder=1)
        ax.scatter(walk[0, 0], walk[0, 1], c='#8fff9f', marker='*', s=100, zorder=2)
        ax.scatter(walk[-1, 0], walk[-1, 1], c='red', marker='*', s=100, zorder=2)
        ax.set_aspect('equal', 'box')
        ax.set_xlim([walk[:, 0].min() - 5, walk[:, 0].max() + 5])
        ax.set_ylim([walk[:, 1].min() - 5, walk[:, 1].max() + 5])
        ax.spines['bottom'].set_color(axis_color)
        ax.spines['top'].set_color(axis_color)
        ax.xaxis.label.set_color(axis_color)
        ax.tick_params(axis='x', colors=axis_color)
        ax.tick_params(axis='y', colors=axis_color)
        fig.patch.set_facecolor(facecolor)
        if titleFlag:
            ax.set_title(f"Walk: {self.directions} Direction, {walk.shape[0] - 1} Steps")
        return fig

    def probsplot(self, facecolor='w', axis_color='k'):

        fig, ax = plt.subplots()
        norm = mcolors.Normalize(vmin=np.min(self.probs), vmax=np.max(self.probs))
        normalized = norm(self.probs)
        colormap = plt.cm.magma
        colors = colormap(normalized)

        for i in range(self.directions):
            ax.plot([0, self.increments[i, 0] * self.probs[i]],
                    [0, self.increments[i, 1] * self.probs[i]],
                    c=colors[i], zorder=1)

        ax.set_aspect('equal', 'box')
        ax.scatter(0, 0, c='r', s=50, marker='o', zorder=2)
        idMax = np.argmax(self.probs)
        idMin = np.argmin(self.probs)
        ax.scatter(self.increments[idMax, 0] * self.probs[idMax],
                   self.increments[idMax, 1] * self.probs[idMax],
                   s=50, c='blue', marker='^')
        ax.scatter(self.increments[idMin, 0] * self.probs[idMax],
                   self.increments[idMin, 1] * self.probs[idMax],
                   s=50, c='blue', marker='v')
        avgDir = self.averageDirection()
        plt.scatter(avgDir[0] * np.mean(self.probs),
                    avgDir[1] * np.mean(self.probs),
                    s=50, marker='x', zorder=3, c='k')
        ax.spines['bottom'].set_color(axis_color)
        ax.spines['top'].set_color(axis_color)
        ax.xaxis.label.set_color(axis_color)
        ax.tick_params(axis='x', colors=axis_color)
        ax.tick_params(axis='y', colors=axis_color)
        fig.patch.set_facecolor(facecolor)
        return fig
