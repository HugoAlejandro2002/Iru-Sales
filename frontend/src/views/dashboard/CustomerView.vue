<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ customer.name }}</h1>

                <div class="buttons">
                    <router-link :to="{ name: 'EditCustomer', params: { id: customer.id }}" class="button is-light">Edit</router-link>
                    <button class="button is-danger" @click="deleteCustomer">Delete</button>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Details</h2>

                    <p><strong>Created at: </strong>{{ customer.created_at }}</p>
                    <p><strong>Modified at: </strong>{{ customer.modified_at }}</p>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact information</h2>

                    <p><strong>Contact person: </strong>{{ customer.contact_person }}</p>
                    <p><strong>Email: </strong>{{ customer.email }}</p>
                    <p><strong>Phone: </strong>{{ customer.phone }}</p>
                    <p><strong>Website: </strong>{{ customer.website }}</p>
                </div>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle">Notes</h2>

                <router-link :to="{ name: 'AddNote', params: { id: customer.id }}" class="button is-success mb-6">Add note</router-link>
            
                <div
                    class="box"
                    v-for="note in notes"
                    v-bind:key="note.id"
                >
                    <h3 class="is-size-4">{{ note.name }}</h3>

                    <p>
                        {{ note.body }}
                    </p>

                    <router-link :to="{ name: 'EditNote', params: { id: customer.id, note_id: note.id }}" class="button is-success mt-6">Edit note</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'Customer',
        data() {
            return {
                customer: {},
                notes: []
            }
        },
        mounted() {
            this.getCustomer()
        },
        methods: {
            async deleteCustomer() {
                this.$store.commit('setIsLoading', true)

                const customerID = this.$route.params.id

                await axios
                    .post(`/api/v1/customers/delete_customer/${customerID}/`)
                    .then(response => {
                        console.log(response.data)

                        this.$router.push('/dashboard/customers')
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            },
            async getCustomer() {
                this.$store.commit('setIsLoading', true)

                const customerID = this.$route.params.id

                await axios
                    .get(`/api/v1/customers/${customerID}/`)
                    .then(response => {
                        this.customer = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

                await axios
                    .get(`/api/v1/notes/?customer_id=${customerID}`)
                    .then(response => {
                        this.notes = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>