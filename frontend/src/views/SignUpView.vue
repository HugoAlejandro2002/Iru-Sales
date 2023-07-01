<template>
    <div class="container">
        <div class="columns is-centered">
            <div class="column is-4">
                <div class="box has-background-light">
                    <h1 class="title">Sign Up</h1>

                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <label>Email</label>
                            <div class="control">
                                <input type="email" name="email" class="input" v-model="email" />
                            </div>
                        </div>

                        <div class="field">
                            <label>Username</label>
                            <div class="control">
                                <input type="text" name="username" class="input" v-model="username" />
                            </div>
                        </div>

                        <div class="field">
                            <label>Password</label>
                            <div class="control">
                                <input type="password" name="password" class="input" v-model="password" />
                            </div>
                        </div>

                        <div class="field">
                            <label>Confirm Password</label>
                            <div class="control">
                                <input type="password" name="confirmPassword" class="input" v-model="confirmPassword" />
                            </div>
                        </div>

                        <div class="notification is-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">
                                {{ error }}
                            </p>
                        </div>

                        <div class="field">
                            <div class="control">
                                <button class="button is-success is-rounded">
                                    Submit
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
  

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'SignUp',
    data() {
        return {
            email: '',
            username: '',
            password: '',
            confirmPassword: '',
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.email === '') {
                this.errors.push('The email is required')
            }
            if (this.username === '') {
                this.errors.push('The username is required')
            }
            if (this.password === '') {
                this.errors.push('The password is required')
            }
            if (this.password !== this.confirmPassword) {
                this.errors.push('The passwords must match')
            }

            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                const formData = {
                    email: this.email,
                    username: this.username,
                    password: this.password
                }

                await axios
                    .post('/api/v1/users/', formData)
                    .then(response => {
                        toast({
                            message: 'Account successfully created',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right'
                        })

                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        console.log(error.response)
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            console.log(error)
                            this.errors.push('Something went wrong!!! Try again.')
                        }
                    })
                this.$store.commit('setIsLoading', false)
            }
        }
    }
}
</script>
