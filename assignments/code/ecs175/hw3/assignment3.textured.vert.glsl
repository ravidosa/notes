#version 300 es

// an attribute will receive data from a buffer
in vec3 a_position;
in vec3 a_normal;
in vec3 a_tangent;
in vec2 a_texture_coord;

// transformation matrices
uniform mat4x4 u_m;
uniform mat4x4 u_v;
uniform mat4x4 u_p;

// output to fragment stage
out vec3 v_position;
out vec2 v_texture_coord;
out mat3 m_tbn;

void main() {

    // transform a vertex from object space directly to screen space
    // the full chain of transformations is:
    // object space -{model}-> world space -{view}-> view space -{projection}-> clip space
    vec4 vertex_position_world = u_m * vec4(a_position, 1.0);
    mat3 normal_matrix = transpose(inverse(mat3(u_m)));

    vec3 N = normalize(normal_matrix * a_normal);
    vec3 T = normalize(normal_matrix * a_tangent);

    T = normalize(T - dot(T, N) * N);
    vec3 B = normalize(cross(N, T));
    mat3 tbn = mat3(T, B, N);

    v_position = vertex_position_world.xyz;
    v_texture_coord = a_texture_coord;
    m_tbn = tbn;

    gl_Position = u_p * u_v * vertex_position_world;

}