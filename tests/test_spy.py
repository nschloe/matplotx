import tempfile
from pathlib import Path

import imageio
import numpy
import pytest
from scipy import sparse

import matplotx


def test_show():
    M = sparse.rand(20, 20, density=0.1)
    plt = matplotx.spy(M)
    plt.show()


@pytest.mark.parametrize(
    "ref, kwargs",
    [
        (6875310, {}),
        (7524085, {"border_width": 1}),
        (21306270, {"border_width": 1, "border_color": "red"}),
        (4981037, {"colormap": "viridis"}),
        (7101351, {"colormap": "viridis", "border_width": 1}),
    ],
)
def test_png(ref, kwargs):
    M = sparse.rand(20, 30, density=0.1, random_state=123)
    numpy.random.seed(123)

    with tempfile.TemporaryDirectory() as temp_dir:
        filepath = Path(temp_dir) / "test.png"
        matplotx.spy(M, filename=filepath, **kwargs)
        im = imageio.imread(filepath)
        y = numpy.random.randint(0, 100, size=numpy.prod(im.shape))
        assert numpy.dot(y, im.flatten()) == ref


def test_readme_images():
    import meshzoo
    from skfem import BilinearForm, ElementTriP2, InteriorBasis, MeshTri
    from skfem.helpers import dot, grad

    @BilinearForm
    def laplace(u, v, _):
        return dot(grad(u), grad(v))

    points, cells = meshzoo.rectangle_tri((-1.0, 1.0, 20), (-1.0, 1.0, 20))
    mesh = MeshTri(points.T, cells.T)

    basis = InteriorBasis(mesh, ElementTriP2())
    A = laplace.assemble(basis)

    with tempfile.TemporaryDirectory() as temp_dir:
        filepath = Path(temp_dir) / "test.png"
        matplotx.spy(A, border_width=2, filename=filepath)

    # betterspy.write_png(
    #     'ATA.png', M, border_width=2,
    #     colormap='viridis'
    #     )


def test_cli():
    this_dir = Path(__file__).resolve().parent
    mmfile = this_dir / "data" / "gre_343_343_crg.mm"
    matplotx.cli(["spy", mmfile.as_posix()])
    matplotx.cli(["spy", mmfile.as_posix(), "out.png"])


if __name__ == "__main__":
    test_readme_images()
