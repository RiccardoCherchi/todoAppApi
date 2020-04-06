<template>
    <v-content id="v-content">
        <div class="table">
            <form @submit.prevent="addTodo">
                <v-text-field
                        placeholder="instert todo and press enter"
                        v-model="message"
                        color="yellow"
                        solo
                        dark
                        class="mb-n3"
                />
            </form>
            <v-card dark class="mt-5 pt-3">
                <h2 class="pb-4 white--text ml-4">
                    Incomplete Todo
                    <v-btn
                            fab dark small
                            color="success"
                            class="toggle-table-icon"
                            @click="toggleTable = !toggleTable">
                        <v-icon class="add-animation" v-if="!toggleTable">add</v-icon>
                        <v-icon class="add-animation" v-else>remove</v-icon>
                    </v-btn>
                </h2>
                <v-simple-table v-if="this.todos.length !== 0 && toggleTable">
                    <template>
                        <thead>
                        <tr>
                            <th v-for="(i, key) in thItems" :key="key">
                                {{ i }}
                            </th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="item in todos" :key="item.id">
                            <template v-if="!item.complete">
                                <td v-if="isOnEdit.id !== item.id" @dblclick="toggleEdit(item.id, todos.indexOf(item))">
                                    {{ item["message"] }}
                                </td>
                                <td v-if="isOnEdit.state && isOnEdit.id === item.id">
                                    <form @submit.prevent="editTodo(item.id, todos.indexOf(item))">
                                        <v-text-field
                                                color="yellow"
                                                placeholder="edit here"
                                                v-model="message"
                                        >
                                        </v-text-field>
                                    </form>
                                </td>
                                <td>{{ item["creation_date"] }}
                                <td>
                                    <v-btn
                                            icon
                                            :color="!item.complete ? 'green' : 'red'"
                                            @click="toggleCompleteTodo(item.id, todos.indexOf(item))"
                                    >
                                        <v-icon v-if="!item.complete">done</v-icon>
                                        <v-icon v-else>clear</v-icon>
                                    </v-btn>
                                </td>
                            </template>
                        </tr>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-card>

            <v-card dark class="mt-8 pt-3" v-if="this.isCompleteTodo">
                <h2 class="pb-4 white--text ml-4">
                    Complete Todo
                    <v-btn
                            fab dark small
                            color="success"
                            class="toggle-table-icon"
                            @click="toggleCompleteTable = !toggleCompleteTable">
                        <v-icon class="add-animation" v-if="!toggleCompleteTable">add</v-icon>
                        <v-icon class="add-animation" v-else>remove</v-icon>
                    </v-btn>
                </h2>
                <v-simple-table v-if="toggleCompleteTable">
                    <template>
                        <thead>
                        <tr>
                            <th v-for="(i, key) in thItemsComplete" :key="key">
                                {{ i }}
                            </th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="item in todos" :key="item.name">
                            <template v-if="item.complete">
                                <td class="complete">{{ item['message'] }}</td>
                                <td>{{ item['creation_date'] }}</td>
                                <td>
                                    <v-btn
                                            color="yellow"
                                            icon
                                            @click="toggleCompleteTodo(item.id, todos.indexOf(item))"
                                    >
                                        <v-icon>remove</v-icon>
                                    </v-btn>
                                </td>
                                <td>
                                    <v-btn
                                            color="red"
                                            icon
                                            @click="deleteTodo(item.id, todos.indexOf(item))"
                                    >
                                        <v-icon>clear</v-icon>
                                    </v-btn>
                                </td>
                            </template>
                        </tr>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-card>
        </div>
    </v-content>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Todo",
        data: () => ({
            thItems: ["Todo", "Time", "Check"],
            thItemsComplete: ["Todo", "Time", "Uncheck", "Delete"],
            isCompleteTodo: 0,
            toggleCompleteTable: true,
            toggleTable: true,
            message: "",
            isOnEdit: {
                state: false,
                id: null
            },
            todos: []
        }),
        methods: {
            addButton() {
                this.isInputActive = !this.isInputActive;
                if (this.isOnEdit.state) {
                    this.clearEditForm()
                }
                this.message = ""
            },
            addTodo() {
                axios
                    .post('http://127.0.0.1:8000/todo/', {
                        "message": this.message,
                        "complete": false,
                        "important": false,
                        "todo_list": 1
                    })
                    .then((response) => {
                        this.todos.push(response.data);
                        this.message = "";
                    })
            },
            deleteTodo: function (key, pos) {
                const {todos} = this;
                window.console.log(key);
                axios
                    .delete(`http://127.0.0.1:8000/todo/${key}/`)
                    .then(() => {
                        todos.splice(pos, 1);
                        if (this.todos.length === 0) {
                            this.isCompleteTodo = 0;
                        }
                        this.todos.forEach((item) => {
                            if (item.complete) {
                                this.isCompleteTodo += 1;
                            } else if (!item.complete) {
                                this.isCompleteTodo -= 1;
                            }
                        })
                    })
            },
            toggleEdit(key, pos) {
                if (!this.isOnEdit.state) {
                    // const editField = document.getElementById("editField");
                    // editField.focus()
                    this.message = this.todos[pos].message;
                    this.isOnEdit = {
                        state: true,
                        id: key
                    };
                } else {
                    this.clearEditForm()
                }
            },
            editTodo(key, pos) {
                axios
                    .put(`http://127.0.0.1:8000/todo/${key}/`, {
                        "message": this.message,
                        "complete": this.todo[pos].complete,
                        "important": this.todo[pos].important,
                        "todo_list": this.todo[pos].todo_list
                    })
                    .then((response) => {
                        this.todos[pos].message = response.data.message;
                        this.clearEditForm()
                    })
            },
            clearEditForm() {
                this.message = "";
                this.isOnEdit = {
                    state: false,
                    id: null,
                }
            },
            toggleCompleteTodo(key, pos) {

                const todo = this.todos[pos];
                axios
                    .put(`http://127.0.0.1:8000/todo/${key}/`, {
                        "message": todo.message,
                        "complete": !todo.complete,
                        "important": todo.important,
                        "todo_list": todo.todo_list
                    })
                    .then((response) => {
                        todo.complete = response.data.complete;
                        if (todo.complete) {
                            this.isCompleteTodo += 1
                        } else {
                            this.isCompleteTodo -= 1
                        }
                    })
            },
        },
        mounted() {
            axios
                .get('http://127.0.0.1:8000/todo/')
                .then((response) => {
                    this.todos = response.data;
                    this.todos.forEach((item) => {
                        if (item.complete) {
                            this.isCompleteTodo = this.isCompleteTodo += 1;
                        } else {
                            this.isCompleteTodo = this.isCompleteTodo === 0 ? this.isCompleteTodo = 0 : this.isCompleteTodo -= 1;
                        }
                    })
                })
        }
    }
</script>

<style scoped lang="scss">
    .table {
        margin: 5% 25% 5%;
        @media (max-width: 758px) {
            margin: 5% 10% 5%;
        }
    }

    .complete {
        color: gray;
        text-decoration-line: line-through;
        transition: color 400ms;
    }

    .toggle-table-icon {
        margin-top: -32px;
        position: absolute;
        right: 2%;
    }
</style>