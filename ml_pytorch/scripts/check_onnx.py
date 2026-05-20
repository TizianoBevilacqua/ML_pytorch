import onnx
from onnx import shape_inference

m = onnx.load("/work/bevila_t/PostDoc/HH4b/Output/ML_trainings/bkg_reweigting_boosted/fourth_test/best_models/best_model_run19.onnx")
print("IR version:", m.ir_version)
print("opset imports:", [(x.domain, x.version) for x in m.opset_import])

# Inputs
print("\n=== Inputs ===")
for i in m.graph.input:
    t = i.type.tensor_type
    dims = [d.dim_value if d.dim_value else d.dim_param for d in t.shape.dim]
    print(i.name, t.elem_type, dims)

# Outputs (as stored)
print("\n=== Outputs (declared) ===")
for o in m.graph.output:
    t = o.type.tensor_type
    dims = [d.dim_value if d.dim_value else d.dim_param for d in t.shape.dim]
    print(o.name, t.elem_type, dims)

# Outputs (after shape inference)
mi = shape_inference.infer_shapes(m)
print("\n=== Outputs (inferred) ===")
for o in mi.graph.output:
    t = o.type.tensor_type
    dims = [d.dim_value if d.dim_value else d.dim_param for d in t.shape.dim]
    print(o.name, t.elem_type, dims)