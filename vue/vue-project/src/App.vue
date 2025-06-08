<script setup>
import { reactive, ref } from 'vue'
import axios from 'axios'

const question = reactive({
  question_text: '',
  choices: [{ choice_text: '', is_correct: false }]
})

const responseMessage = ref('')

function addChoice() {
  question.choices.push({ choice_text: '', is_correct: false })
}

async function submitQuestion() {
  try {
    const response = await axios.post('http://localhost:8000/questions/', question)
    responseMessage.value = response.data.message
  } catch (error) {
    console.error(error)
    responseMessage.value = 'Fehler beim Absenden!'
  }
}
</script>

<template>
  <div class="app-container">
    <h1>Frage erstellen</h1>
    <form @submit.prevent="submitQuestion" class="form-container">
      <div class="input-field">
        <label for="question-text">Frage:</label>
        <input v-model="question.question_text" placeholder="Frage eingeben" id="question-text" />
      </div>

      <div v-for="(choice, index) in question.choices" :key="index" class="choice">
        <div class="input-field">
          <input v-model="choice.choice_text" placeholder="Antwort" />
          <label>
            <input type="checkbox" v-model="choice.is_correct" />
            Richtig?
          </label>
        </div>
      </div>

      <button type="button" @click="addChoice" class="button">Antwort hinzufügen</button>
      <button type="submit" class="button submit">Absenden</button>
    </form>

    <p v-if="responseMessage" class="response-message">{{ responseMessage }}</p>
  </div>
</template>

<style>
html, body, #app {
  height: 100%;
  margin: 0;
  padding: 0;
  background: #181a1b; /* sehr dunkles Grau, angenehmer als reines Schwarz */
  color: #f1f1f1;
}

body, #app {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.app-container {
  background: #23272a;
  padding: 2rem 2.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.3);
  min-width: 650px;    /* vorher 500px, jetzt breiter */
  max-width: 900px;    /* optional, damit es nicht zu breit wird */
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #f1f1f1;
}

.form-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.input-field {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

input, textarea {
  background: #181a1b;
  color: #f1f1f1;
  border: 1px solid #444;
  border-radius: 5px;
  padding: 0.5rem;
  width: 100%;         /* nimmt die volle Breite des Containers ein */
  box-sizing: border-box;
  font-size: 1.1rem;
}

input[type="checkbox"] {
  accent-color: #4caf50;
}

.choice {
  margin-bottom: 0.5rem;
}

.button {
  margin-right: 0.5rem;
  padding: 0.5rem 1.2rem;
  border: none;
  border-radius: 6px;
  background: #4caf50;
  color: white;
  cursor: pointer;
  transition: background 0.2s;
}

.button.submit {
  background: #007bff;
}

.button:hover {
  background: #388e3c;
}

.response-message {
  margin-top: 1.2rem;
  font-weight: bold;
  color: #f1f1f1;
}

</style>

