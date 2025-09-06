import os, numpy as np, trimesh as t, plotly.graph_objects as g

p = r"C:\Users\Paul\Desktop\beam.stl"
u = True
v = True

def f(o):
    if isinstance(o, t.Scene):
        r = []
        for n, m in o.geometry.items():
            T = o.graph.get(world=n)[0] if o.graph.nodes_geometry else np.eye(4)
            q = m.copy()
            q.apply_transform(T)
            r.append((n or "m", q))
        return r
    elif isinstance(o, t.Trimesh):
        return [(os.path.basename(p), o)]
    else:
        raise TypeError("x")

def c(m: t.Trimesh):
    m.remove_unreferenced_vertices()
    m.update_faces(m.unique_faces())
    m.update_faces(m.nondegenerate_faces())
    m.merge_vertices()
    m.fix_normals()
    if m.is_winding_consistent is False:
        m.invert()
    return m

o = t.load(p, skip_materials=True)
a = f(o)
a = [(n, c(m)) for n, m in a]

if v:
    R = t.transformations.rotation_matrix(np.deg2rad(-90), [1,0,0])
    for _, m in a:
        m.apply_transform(R)

if u:
    for _, m in a:
        m.apply_scale(0.001)

b = t.util.concatenate([m for _, m in a]).bounding_box
d = b.centroid
for _, m in a:
    m.apply_translation(-d)

s = t.Scene()
for n, m in a:
    s.add_geometry(m, node_name=n)
q = os.path.join(os.path.dirname(p), "fixed.glb")
s.export(q)
print("Wrote:", q)

h = []
k = ["lightgray","tomato","goldenrod","lightseagreen","slateblue"]
for i, (n, m) in enumerate(a):
    x,y,z = m.vertices.T; I,J,K = m.faces.T
    h.append(g.Mesh3d(x=x,y=y,z=z,i=I,j=J,k=K,
                      color=k[i%len(k)],
                      flatshading=True, opacity=1.0,
                      name=n))
f2 = g.Figure(h)
f2.update_layout(scene_aspectmode="data")
f2.show()
