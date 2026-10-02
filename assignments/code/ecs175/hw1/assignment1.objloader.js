import { loadExternalFile } from './js/utils/utils.js'

/**
 * A class to load OBJ files from disk
 */
class OBJLoader {

    /**
     * Constructs the loader
     *
     * @param {String} filename The full path to the model OBJ file on disk
     */
    constructor(filename) {
        this.filename = filename
    }

    /**
     * Loads the file from disk and parses the geometry
     *
     * @returns {[Array<Number>, Array<Number>]} A tuple / list containing 1) the list of vertices and 2) the list of triangle indices
     */
    load() {
        // Load the file's contents
        let contents = loadExternalFile(this.filename)

        // Create lists for vertices and indices
        let vertices = []
        let indices = []

        let lines = contents.split("\n")

        lines.forEach((line) => {
            let l = line.trim()
            if (l.length > 0) {
                if (l.startsWith("v")) {
                    let v = this.parseVertex(l)
                    vertices.push(...v)
                }
                if (l.startsWith("f")) {
                    let f = this.parseFace(l)
                    indices.push(...f)
                }
            }

        })

        if (vertices.length > 0) {
            let minx = Infinity, maxx = -Infinity
            let miny = Infinity, maxy = -Infinity
            let minz = Infinity, maxz = -Infinity

            for (let i = 0; i < vertices.length; i += 3) {
                minx = Math.min(minx, vertices[i])
                maxx = Math.max(maxx, vertices[i])
                miny = Math.min(miny, vertices[i + 1])
                maxy = Math.max(maxy, vertices[i + 1])
                minz = Math.min(minz, vertices[i + 2])
                maxz = Math.max(maxz, vertices[i + 2])
            }

            let centerx = (minx + maxx) / 2
            let centery = (miny + maxy) / 2
            let centerz = (minz + maxz) / 2
            let range = Math.max(maxx - minx, maxy - miny, maxz - minz)

            if (range > 0) {
                for (let i = 0; i < vertices.length; i += 3) {
                    vertices[i] = (vertices[i] - centerx) / range * 2
                    vertices[i + 1] = (vertices[i + 1] - centery) / range * 2
                    vertices[i + 2] = (vertices[i + 2] - centerz) / range * 2
                }
            }
        }

        return [ vertices, indices ]
    }

    /**
     * Parses a single OBJ vertex entry given as a string
     * Call this function from OBJLoader.load()
     *
     * @param {String} vertex_string String containing the vertex entry 'v {x} {y} {z}'
     * @returns {Array<Number>} A list containing the x, y, z coordinates of the vertex
     */
    parseVertex(vertex_string)
    {
        let coords = vertex_string.split(/\s+/)
        let x = parseFloat(coords[1])
        let y = parseFloat(coords[2])
        let z = parseFloat(coords[3])
        return [x, y, z]
    }

    /**
     * Parses a single OBJ face entry given as a string
     * Face entries can refer to 3 or 4 elements making them triangle or quad faces
     * WebGL only supports triangle drawing, so we need to triangulate the entry if we find 4 indices
     * This is done using OBJLoader.triangulateFace()
     *
     * Each index entry can have up to three components separated by '/'
     * You need to grad the first component. The other ones are for textures and normals which will be treated later
     * Make sure to account for this fact.
     *
     * Call this function from OBJLoader.load()
     *
     * @param {String} face_string String containing the face entry 'f {v0}/{vt0}/{vn0} {v1}/{vt1}/{vn1} {v2}/{vt2}/{vn2} ({v3}/{vt3}/{vn3})'
     * @returns {Array<Number>} A list containing three indices defining a triangle
     */
    parseFace(face_string)
    {
        let coords = face_string.split(/\s+/)
        let inds = []
        for (let i = 1; i < coords.length; i++) {
            let vind = parseInt(coords[i].split("/")[0])
            inds.push(vind - 1)
        }
        return inds
    }

    /**
     * Triangulates a face entry given as a list of 4 indices
     * Use these 4 indices to create indices for two separate triangles that share a side (2 vertices)
     * Return a new index list containing the triangulated indices
     *
     * @param {Array<Number>} face The quad indices with 4 entries
     * @returns {Array<Number>} The newly created list containing triangulated indices
     */
    triangulateFace(face)
    {
        return [face[0], face[1], face[2], face[0], face[2], face[3]]
    }
}

export {
    OBJLoader
}
