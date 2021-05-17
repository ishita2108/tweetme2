import React from 'react';
import {apiTweetAction} from './lookup'

export function ActionBtn(props){
   const {tweet, action, didPerformAction} = props
   const likes = tweet.likes ? tweet.likes : 0
  //  const [likes, setLikes] = useState()
  //  const [userLike, setUserLike] = useState(tweet.userLike === true ? true : false)
   const className= props.className ?props.className : 'btn btn-info btn-small'
   const actionDisplay = action.display ? action.display: 'Action'
   const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay

  const handleActionBackendEvent = (response, status) =>{
    console.log(status, response) 
    if ((status === 200 || status === 201) && didPerformAction){
      //setLikes(response.likes)
      didPerformAction(response, status)
      // setUserLike(true)
    }

      // if (action.type === 'like'){
      //     if(userLike === true){
      //         //perhaps i unlike it?
      //         setLikes(likes - 1)
      //         setUserLike(false)
      //     }
      //     else{
      //         setLikes(likes + 1)
      //         setUserLike(true)
      //     }
      // }
  }

   const handleClick =(event) =>{
       event.preventDefault()
       apiTweetAction(tweet.id, action.type, handleActionBackendEvent)  
   }
      return <button className={className} onClick={handleClick}>{display}</button>
    }