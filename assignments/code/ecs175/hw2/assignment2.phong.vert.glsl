#version 300 es

precision mediump float;

// an attribute will receive data from a buffer
in vec3 a_position;
in vec3 a_normal;

// transformation matrices
uniform mat4x4 u_m;
uniform mat4x4 u_v;
uniform mat4x4 u_p;

// output to fragment stage
out vec3 v_normal;
out vec3 v_position;

void main() {

    vec4 world_position = u_m * vec4(a_position, 1.0);
    mat3 normal_matrix = transpose(inverse(mat3(u_m)));
    vec3 world_normal = normal_matrix * a_normal;
    v_position = world_position.xyz;
    v_normal = world_normal;
    gl_Position = u_p * u_v * world_position;
}
