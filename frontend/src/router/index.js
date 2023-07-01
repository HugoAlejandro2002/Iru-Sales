import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'
import DashBoardView from '../views/dashboard/DashBoardView.vue'
import MyAccountView from '../views/dashboard/MyAccountView.vue'
import LeadsView from '../views/dashboard/LeadsView.vue'
import AddLeadView from '../views/dashboard/AddLeadView.vue'
import LeadView from '../views/dashboard/LeadView.vue'
import EditLeadView from '../views/dashboard/EditLeadView.vue'
import TeamView from '../views/dashboard/TeamView.vue'
import AddTeamView from '../views/dashboard/AddTeamView.vue'
import AddMemberView from '../views/dashboard/AddMemberView.vue'
import CustomersView from '../views/dashboard/CustomersView.vue'
import AddCustomerView from '../views/dashboard/AddCustomerView.vue'
import CustomerView from '../views/dashboard/CustomerView.vue'
import EditCustomerView from '../views/dashboard/EditCustomerView.vue'
import EditNoteView from '../views/dashboard/EditNoteView.vue'
import AddNoteView from '../views/dashboard/AddNoteView.vue'
import EditMemberView from '../views/dashboard/EditMemberView.vue'
import PlansView from '../views/dashboard/PlansView.vue'


import store from '@/store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      requireLogin: true

    }
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUpView,
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogInView,
  },
  {
    path: '/dashboard',
    name: 'DashBoard',
    component: DashBoardView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccountView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads',
    name: 'Leads',
    component: LeadsView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads/add',
    name: 'AddLead',
    component: AddLeadView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads/:id',
    name: 'Lead',
    component: LeadView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/add-team',
    name: 'AddTeam',
    component: AddTeamView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads/:id/edit',
    name: 'EditLead',
    component: EditLeadView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team',
    name: 'Team',
    component: TeamView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team/add-member',
    name: 'AddMember',
    component: AddMemberView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/customers',
    name: 'Customers',
    component: CustomersView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/customers/add',
    name: 'AddCustomer',
    component: AddCustomerView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/customers/:id',
    name: 'Customer',
    component: CustomerView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/customers/:id/edit',
    name: 'EditCustomer',
    component: EditCustomerView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/:id/add-note',
    name: 'AddNote',
    component: AddNoteView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/:id/edit-note/:note_id',
    name: 'EditNote',
    component: EditNoteView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/edit-member/:id',
    name: 'EditMember',
    component: EditMemberView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team/plans',
    name: 'Plans',
    component: PlansView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }, {

  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }
})

export default router
