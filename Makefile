run-model:
	docker model run ai/mistral

run-app:
	poetry run streamlit run docker_model_app/app.py