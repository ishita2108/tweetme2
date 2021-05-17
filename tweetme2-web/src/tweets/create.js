import React from 'react';
import {apiTweetCreate} from './lookup';


export function TweetCreate(props){
  const textAreaRef = React.createRef()
  const {didTweet} = props

  const handleBackendupdate = (response, status)=>{
    if(status === 201){
      didTweet(response)
    }
    else{
      console.log(response)
      alert("An error occured, please try again!!")
    }
  }

  const handleSubmit = (event) =>{
      event.preventDefault()
      // console.log(event)
      // console.log(textAreaRef.current.value)
      const newVal = textAreaRef.current.value
      //backend api request handler
      // console.log(newVal)
      apiTweetCreate(newVal, handleBackendupdate)
      textAreaRef.current.value = ''
  }

  return <div className={props.className}>
      <form onSubmit={handleSubmit}>
          <textarea ref={textAreaRef} required={true} name = "tweet"  className="form-control"></textarea>
          <button type="submit" className="btn btn-primary my-3">Tweet Now</button>
          
      </form>
  </div>
}
