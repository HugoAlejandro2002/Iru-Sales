<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit {{ customer.name }}</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="customer.name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Contact person</label>
                        <div class="control">
                            <input type="text" class="input" v-model="customer.contact_person">
                        </div>
                    </div>

                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" class="input" v-model="customer.email">
                        </div>
                    </div>

                    <div class="field">
                        <label>Phone</label>
                        <div class="control">
                            <input type="text" class="input" v-model="customer.phone">
                        </div>
                    </div>

                    <div class="field">
                        <label>Website</label>
                        <div class="control">
                            <input type="text" class="input" v-model="customer.website">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Update</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    import { toast } from 'bulma-toast'

    export default {
        name: 'EditCustomer',
        data() {
            return {
                customer: {}
            }
        },
        mounted() {
            this.getCustomer()
        },
        methods: {
            async getCustomer() {
                this.$store.commit('setIsLoading', true)

                const customerID = this.$route.params.id

                axios
                    .get(`/api/v1/customers/${customerID}/`)
                    .then(response => {
                        this.customer = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            },
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const customerID = this.$route.params.id

                axios
                    .patch(`/api/v1/customers/${customerID}/`, this.customer)
                    .then(response => {
                        toast({
                            message: 'The lead was updated',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push(`/dashboard/customers/${customerID}`)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>