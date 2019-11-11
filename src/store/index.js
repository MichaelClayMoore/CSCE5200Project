import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    documents: [],
    results: []
  },
  mutations: {
    add_document_to_store(state,doc){
      state.documents.push(doc)
    },
    set_documents(state, list_of_docs){
      state.documents = list_of_docs
    },
    set_results(state, list_of_results){
      state.results = list_of_results
    }
  },
  actions: {
    getTest({commit, rootState}){
      axios.get('http://127.0.0.1:5000/test')
      .then( response => {
        console.log("response: ", response);
      }), (err) => {
        console.log(err)
      }
    },
    get_docs({commit, rootState}){
      axios.get('http://127.0.0.1:5000/get_docs')
      .then( response => {
        console.log("get_docs reponse: ", response)
        let list_of_docs = response.data;
        commit('set_documents', list_of_docs);
      }), (err) => {
        console.log(err)
        // reject("error");
      }
    },
    add_document({dispatch, commit, rootState}, payload){
      axios.post('http://127.0.0.1:5000/add_document',{
        params: { file_object: payload }
      })
      .then( response => {

        // print response
        console.log("add_document reponse: ", response)

        dispatch('get_docs', null, { root: true })
      }), (err) => {
        console.log(err)
        // reject("error");
      }
    },
    query_documents({commit, rootState}, query){
      axios.get('http://127.0.0.1:5000/query_documents',{
        params: { query: query }
      })
      .then( response => {
        console.log("query_documents reponse: ", response)
        let list_of_results = response.data;
        commit('set_results', list_of_results);
      }), (err) => {
        console.log(err)
        // reject("error");
      }
    }
  },
  modules: {
  }
})
