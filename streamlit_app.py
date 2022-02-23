import streamlit as st
import streamlit_book as stb
from pathlib import Path

def main():
       # Streamlit webpage properties
       st.set_page_config(layout="wide", page_title="Streamlit Book", page_icon="📖",)

       # Streamit book properties
       save_answers = True
       current_path = Path(__file__).parent.absolute()
       stb.set_book_config(menu_title="streamlit_book",
                            menu_icon="lightbulb",
                            options=[
                                          "What's new on v0.7.0?",   
                                          "Core Features", 
                                          "Multipages", 
                                          "Answers", 
                                          "Admin View", 
                                          ], 
                            paths=[
                                          current_path / "pages/00_whats_new.py", 
                                          current_path / "pages/01 Multitest", 
                                          current_path / "pages/02_multipage.py",
                                          current_path / "pages/03_answers.py",
                                          current_path / "pages/04_admin_view.py",
                                   ],
                            icons=[
                                          "code", 
                                          "robot", 
                                          "book", 
                                          "pin-angle", 
                                          "file-earmark-ruled",
                                   ],
                            save_answers=save_answers,
                            )


if __name__ == "__main__":
       main()