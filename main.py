import numpy as np

def h(n0,n1,M):
    """
    Crée un signal pour une moyenne glissante.

    Args:
        n0 (int): Début de la fenêtre de moyenne mobile.
        n1 (int): Fin de la fenêtre de moyenne mobile.
        M  (int): Longueur de la moyenne mobile.

    Returns:
        w (Array numpy): Liste des valeurs du signal de la moyenne mobile.
    """
    n = np.arange(-5,M+5)
    w = np.zeros_like(n,dtype=float)
    w[(n>=n0)&(n<n1)]= 1/M
    return w,n
a,b = h(4,10,15)
print(a,b)