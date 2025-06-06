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
  <div class="container">
    <h1>Frage erstellen</h1>

    <form @submit.prevent="submitQuestion">
      <label>Frage:</label>
      <input v-model="question.question_text" placeholder="Frage eingeben" />

      <div v-for="(choice, index) in question.choices" :key="index" class="choice">
        <input v-model="choice.choice_text" placeholder="Antwort" />
        <label>
          <input type="checkbox" v-model="choice.is_correct" />
          Richtig?
        </label>
      </div>

      <button type="button" @click="addChoice">Antwort hinzufügen</button>
      <button type="submit">Absenden</button>
    </form>

    <p v-if="responseMessage">{{ responseMessage }}</p>
  </div>
</template>

<style>
.container {
  max-width: 600px;
  margin: auto;
  padding: 2rem;
}
.choice {
  margin-bottom: 1rem;
}
</style>
