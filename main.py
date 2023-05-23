import controller.controllerZoo as controller
import streamlit as st
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.set_page_config(
        page_title= "Zoo Cali",
        layout = "wide" ,
        page_icon= "🦚"
    )
    program = controller.controllerZoo()
    program.menuZoo()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
