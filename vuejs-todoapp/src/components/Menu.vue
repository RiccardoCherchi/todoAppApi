<template>
    <v-content id="v-content">
        <div class="menu-container">
            <div>
                {{ msg }}
                <v-card
                        class="menu-item mt-2"
                        :style="{backgroundColor: getRandomColor()}"
                        @click="redirectToTodo"
                        v-for="(card, key) in cards"
                        :key="key"
                        dark
                >
                    <p class="item-link">{{ card }}</p>
                    <v-btn
                            class="item-icon"
                            @click.stop
                            @click="alertButton()"
                            icon
                    >
                        <v-icon>more_vert</v-icon>
                    </v-btn>
                </v-card>
            </div>
        </div>
    </v-content>
</template>

<script>
    import colors from '../assets/colors'

    export default {
        name: "Menu",
        data() {
            return {
                cards: ["test", "come", "va"],
                colors: colors,
                msg: ""
            }
        },
        methods: {
            getRandomColor() {
                let keys = Object.keys(this.colors);
                return this.colors[keys[keys.length * Math.random() << 0]];
            },
            alertButton(msg) {
                alert(msg ? msg : "clicked")
            },
            redirectToTodo() {
                this.$router.push("todo")
            }
        }
    }
</script>

<style scoped lang="scss">

    .menu-item {
        width: 200px;
        height: 100px;
        margin: 10px;
        display: inline-block;

        .item-link {
            color: #fff;
            text-decoration: none;
            margin: 10px;
            font-size: 115%;
            text-shadow: 0 0 5px gray;
        }
    }

    .menu-container {
        width: 70%;
        margin: 2rem auto 0;
        display: flex;
        justify-content: space-evenly;
        flex-wrap: wrap;
    }

    .item-icon {
        position: absolute;
        top: 5%;
        right: 3%;
    }
</style>