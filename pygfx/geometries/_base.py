import numpy as np

from ..datawrappers import Buffer


class Geometry:
    """ A geometry represents the (input) data of mesh, line, or point
    geometry. It can include vertex positions, normals, colors, uvs,
    and custom data buffers. Face indices can be given using `index`.

    Buffer data can be provided as kwargs, these are converted to numpy arrays
    (if necessary) and wrapped in a Buffer.

    Example:

        g = Geometry(positions=[[1, 2], [2, 4], [3, 5], [4, 1]])
        g.positions.data  # numpy array

    """

    def __init__(self, **data):
        for name, val in data.items():
            if not isinstance(val, np.ndarray):
                val = np.asanyarray(val, dtype=np.float32)
            elif val.dtype == np.float64:
                raise ValueError(
                    "64-bit float is not supported, use 32-bit floats instead"
                )
            if name == "positions":
                usage = "vertex|storage"
                # todo: we could auto-convert to Nx4 here
                # ... and we could autoconvert any Nx3 to Nx4
            elif name == "index":
                usage = "index|storage"
            else:
                usage = "vertex|storage"
            setattr(self, name, Buffer(val, usage=usage))