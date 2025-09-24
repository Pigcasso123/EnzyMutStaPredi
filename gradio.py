import gradio as gr
def predict_ddg(mutation, volume):
    return predictor.predict(pd.DataFrame([[mutation, volume]], columns=['mutation', 'cavity_volume']))

iface = gr.Interface(
    fn=predict_ddg,
    inputs=[
        gr.Dropdown(["V108L", "S153A", "H411Q"], label="突变位点"),
        gr.Slider(0.5, 5, label="空腔体积(Å³)")
    ],
    outputs="text",
    title="酶突变稳定性预测器"
)
iface.launch()