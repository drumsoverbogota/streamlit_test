def task(lb,ub,refreshtime,col):
    with col:
        mes="[ "+str(lb)+" , "+str(ub)+" ] "+" time = "+str(refreshtime)
        st.text(mes)
        
        message = "Hello, World!"
        text_element = st.text(message)
        while(1):
            num=r.randint(lb,ub)
        # text_element = st.text(num)
            text_element.text(num)
            # display(num,col)
            # print(num)
            # st.write(num)
            time.sleep(refreshtime)
        return