# Polygon
discrete, computation with curves
polygon: closed region of plane bounded by finite collection of line segments forming closed, non self-intersecting curve
	edges, vertices
	polygonal [jordan curve](jordan-curve.md): boundary $\partial P$ of polygon $P$ partitions plane into bounded interior, unbounded exterior
		path between interior and exterior crosses boundary
		some path within interior/exterior doesn't cross boundary
	diagonal: line segment connecting two vertices (intersection of edges), completely contained in interior
		polygon has diagonal if more than 3 vertices
		crossing vs noncrossing
## Triangulation
[triangulation](https://en.wikipedia.org/wiki/Polygon_triangulation): decomposition of polygon into triangles by maximal set of noncrossing diagonals
every polygon has triangulation
	if $n$ vertices, $n-2$ triangles, $n-3$ diagonals
[ear](https://en.wikipedia.org/wiki/Vertex_(geometry)#Ears): three consecutive vertices, nonadjacent are diagonal
	more than three vertices, at least two ears
	for convex $n+2$-gon, number of triangulations is $\frac{1}{n+1}{2n \choose n}$ ([catalan numbers](https://en.wikipedia.org/wiki/Catalan_number), dyck paths)
	[art gallery problem](https://en.wikipedia.org/wiki/Art_gallery_problem): how many guards such that entire polygon in sight (at least $\lfloor n/3 \rfloor$)
tetrahedralization: extension to 3D with polyhedron
	[schonhardt polyhedron](https://en.wikipedia.org/wiki/Sch%C3%B6nhardt_polyhedron): untetrahedralizable with fewest vertices (6)
	determining if tetrahedralizable is [np complete](class-np.md)
3-colorable (by induction)
[rectilinear crossing number](http://www.ist.tugraz.at/staff/aichholzer/research/rp/triangulations/crossing/)
## Chirotopes
order type: orientations of triples
checking if point inside polygon
	shoot random ray, check parity of boundary crossings
	[chirotrope](https://en.wikipedia.org/wiki/Oriented_matroid): using determinant, higher dimension generalization
		antisymmetric
## Area
area by determinant
	triangle: $\begin{vmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{vmatrix}$
		pick a point, cycle through
	convex polygon: shoelace
	nonconvex: choose point, add triangle areas