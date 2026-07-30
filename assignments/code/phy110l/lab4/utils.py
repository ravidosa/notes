import numpy as np
def relaxation(Vgrid, boundary_mask, eps, cond=None):
    ch = 1
    iter = 0
    while ch > eps:
        if cond == "periodic":
            V_rel = 1 / 4 * (np.roll(Vgrid, 1, 0) + np.roll(Vgrid, -1, 0) + np.roll(Vgrid, 1, 1) + np.roll(Vgrid, -1, 1))
        elif cond == "periodicx":
            V_rel = 1 / 4 * (np.pad(Vgrid,((1,0),(0,0)), mode='edge')[:-1, :] + np.pad(Vgrid,((0,1),(0,0)), mode='edge')[1:, :] + np.roll(Vgrid, 1, 1) + np.roll(Vgrid, -1, 1))
        elif cond == "periodicy":
            V_rel = 1 / 4 * (np.roll(Vgrid, 1, 0) + np.roll(Vgrid, -1, 0) + np.pad(Vgrid,((0,0),(1,0)), mode='edge')[:, :-1] + np.pad(Vgrid,((0,0),(0,1)), mode='edge')[:, 1:])
        else:
            V_rel = 1 / 4 * (np.pad(Vgrid,((1,0),(0,0)), mode='edge')[:-1, :] + np.pad(Vgrid,((0,1),(0,0)), mode='edge')[1:, :] + np.pad(Vgrid,((0,0),(1,0)), mode='edge')[:, :-1] + np.pad(Vgrid,((0,0),(0,1)), mode='edge')[:, 1:])
        V_rel[boundary_mask] = Vgrid[boundary_mask]
        ch = np.nanmax(np.abs((V_rel - Vgrid) / (np.abs(Vgrid * (Vgrid==0) + (Vgrid != 0)))))
        Vgrid = V_rel.copy()
        iter += 1
    return Vgrid, iter
def V_boundary_hollowsquare(center, side, V, xgrid, ygrid):
    centerx, centery = center
    s1 = np.logical_and(xgrid == centerx + side / 2, np.abs(ygrid - centery) <= side / 2)
    s2 = np.logical_and(xgrid == centerx - side / 2, np.abs(ygrid - centery) <= side / 2)
    s3 = np.logical_and(ygrid == centery + side / 2, np.abs(xgrid - centerx) <= side / 2)
    s4 = np.logical_and(ygrid == centery - side / 2, np.abs(xgrid - centerx) <= side / 2)
    boundary_mask = np.logical_or(s1, np.logical_or(s2, np.logical_or(s3, s4)))
    Vgrid = V * boundary_mask
    return boundary_mask, Vgrid
def V_boundary_infinity(center, radius, V, xgrid, ygrid):
    centerx, centery = center
    rgrid1, thgrid1 = np.hypot(xgrid - centerx + radius, ygrid - centery), np.arctan2(xgrid - centerx + radius, ygrid - centery)
    rgrid2, thgrid2 = np.hypot(xgrid - centerx - radius, ygrid - centery), np.arctan2(xgrid - centerx - radius, ygrid - centery)
    boundary_mask = np.logical_or(np.abs(rgrid1 - radius) <= 0.5, np.abs(rgrid2 - radius) <= 0.5)
    Vgrid = V * (np.sin(2 * thgrid1) + np.sin(-2 * thgrid2)) * boundary_mask
    return boundary_mask, Vgrid
def V_boundary_infplates(center, width, V, xgrid, ygrid):
    centerx, centery = center
    boundary_mask = np.logical_or(np.abs(ygrid - centery) == width / 2, np.logical_or(ygrid == np.max(ygrid), ygrid == np.min(ygrid)))
    Vgrid = V * ((ygrid == centery - width / 2).astype(int) - (ygrid == centery + width / 2).astype(int)) * boundary_mask
    return boundary_mask, Vgrid
def V_boundary_infplates_corr(center, width, V, xgrid, ygrid):
    centerx, centery = center
    boundary_mask = np.abs(np.abs(ygrid - centery) - (width / 2 + 0.5)) <= 0.5
    Vgrid = V * ((ygrid == centery - width / 2).astype(int) - (ygrid == centery + width / 2).astype(int)) * boundary_mask
    return boundary_mask, Vgrid