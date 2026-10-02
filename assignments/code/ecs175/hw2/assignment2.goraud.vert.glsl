#version 300 es

precision mediump float;

#define MAX_LIGHTS 16

// struct definitions
struct AmbientLight {
    vec3 color;
    float intensity;
};

struct DirectionalLight {
    vec3 direction;
    vec3 color;
    float intensity;
};

struct PointLight {
    vec3 position;
    vec3 color;
    float intensity;
};

struct Material {
    vec3 kA;
    vec3 kD;
    vec3 kS;
    float shininess;
};


// an attribute will receive data from a buffer
in vec3 a_position;
in vec3 a_normal;

// camera position
uniform vec3 u_eye;

// transformation matrices
uniform mat4x4 u_m;
uniform mat4x4 u_v;
uniform mat4x4 u_p;

// lights and materials
uniform AmbientLight u_lights_ambient[MAX_LIGHTS];
uniform DirectionalLight u_lights_directional[MAX_LIGHTS];
uniform PointLight u_lights_point[MAX_LIGHTS];

uniform Material u_material;

// shading output
out vec4 o_color;

// Shades an ambient light and returns this light's contribution
vec3 shadeAmbientLight(Material material, AmbientLight light) {
    
    return material.kA * light.color * light.intensity;
}

// Shades a directional light and returns its contribution
vec3 shadeDirectionalLight(Material material, DirectionalLight light, vec3 normal, vec3 eye, vec3 vertex_position) {

    vec3 N = normalize(normal);
    vec3 L = normalize(light.direction);
    vec3 V = normalize(eye - vertex_position);
    vec3 R = reflect(-L, N);

    vec3 diffuse = material.kD * light.color * light.intensity * max(dot(N, L), 0.0);
    vec3 specular = material.kS * light.color * light.intensity * pow(max(dot(R, V), 0.0), material.shininess);

    return diffuse + specular;
}

// Shades a point light and returns its contribution
vec3 shadePointLight(Material material, PointLight light, vec3 normal, vec3 eye, vec3 vertex_position) {

    vec3 N = normalize(normal);
    vec3 L = normalize(light.position - vertex_position);
    float D = distance(light.position, vertex_position);
    vec3 V = normalize(eye - vertex_position);
    vec3 R = reflect(-L, N);

    vec3 diffuse = material.kD * light.color * light.intensity * max(dot(N, L), 0.0);
    vec3 specular = material.kS * light.color * light.intensity * pow(max(dot(R, V), 0.0), material.shininess);

    return (diffuse + specular) / (D * D + 1.0);
}

void main() {

    vec4 world_position = u_m * vec4(a_position, 1.0);
    vec3 vertex_position = world_position.xyz;
    mat3 normal_matrix = transpose(inverse(mat3(u_m)));
    vec3 world_normal = normal_matrix * a_normal;
    vec3 light = vec3(0.0);

    for (int i = 0; i < MAX_LIGHTS; i++) {
        light += shadeAmbientLight(u_material, u_lights_ambient[i]);
        light += shadeDirectionalLight(u_material, u_lights_directional[i], world_normal, u_eye, vertex_position);
        light += shadePointLight(u_material, u_lights_point[i], world_normal, u_eye, vertex_position);
    }

    light = clamp(light, 0.0, 1.0);
    o_color = vec4(light, 1.0);
    gl_Position = u_p * u_v * world_position;
}