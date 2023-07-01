<template>
    <div class="container">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h1 class="title">Customers</h1>
        </div>
  
        <div class="column is-12">
          <div class="field is-grouped">
            <div class="control">
              <router-link
                to="/dashboard/customers/add"
                v-if="$store.state.team.max_customers > num_customers"
                class="button is-primary is-rounded"
              >
                Add customer
              </router-link>
            </div>
            <div class="control">
              <form @submit.prevent="getCustomers">
                <div class="field has-addons">
                  <div class="control">
                    <input type="text" class="input" v-model="query" />
                  </div>
                  <div class="control">
                    <button class="button is-success is-rounded">Search</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
  
          <hr />
  
          <template v-if="customers.length">
            <table class="table is-fullwidth">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Contact person</th>
                  <th></th>
                </tr>
              </thead>
  
              <tbody>
                <tr v-for="customer in customers" v-bind:key="customer.id">
                  <td>{{ customer.name }}</td>
                  <td>{{ customer.contact_person }}</td>
                  <td>
                    <router-link
                      :to="{ name: 'Customer', params: { id: customer.id } }"
                      class="button is-link is-rounded"
                    >
                      Details
                    </router-link>
                  </td>
                </tr>
              </tbody>
            </table>
  
            <div class="buttons">
              <button
                class="button is-light is-rounded"
                @click="goToPreviousPage()"
                v-if="showPreviousButton"
              >
                Previous
              </button>
              <button
                class="button is-light is-rounded"
                @click="goToNextPage()"
                v-if="showNextButton"
              >
                Next
              </button>
            </div>
          </template>
  
          <template v-else>
            <p>You don't have any customers yet...</p>
          </template>
        </div>
      </div>
    </div>
  </template>
  

<script>
import axios from 'axios'

export default {
    name: 'Customers',
    data() {
        return {
            customers: [],
            showNextButton: false,
            showPreviousButton: false,
            currentPage: 1,
            query: '',
            num_customers: 0
        }
    },
    mounted() {
        this.getCustomers()
    },
    methods: {
        goToNextPage() {
            this.currentPage += 1
            this.getCustomers()
        },
        goToPreviousPage() {
            this.currentPage -= 1
            this.getCustomers()
        },
        async getCustomers() {
            this.$store.commit('setIsLoading', true)

            this.showNextButton = false
            this.showPreviousButton = false

            await axios
                .get(`/api/v1/customers/`)
                .then(response => {
                 

                    this.num_customers = response.data.count
                })

            await axios
                .get(`/api/v1/customers/?page=${this.currentPage}&search=${this.query}`)
                .then(response => {
                    this.customers = response.data.results
                    console.log(response.data)

                    if (response.data.next) {
                        this.showNextButton = true
                    }

                    if (response.data.previous) {
                        this.showPreviousButton = true
                    }
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>