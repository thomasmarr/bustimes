import React from 'react'
import * as S from './Styles'

const ErrorBox = ({message, refresh}) => {
    return (
      <S.ErrorBox>
        <p>{message}</p>
        <S.Button onClick={refresh} className="btn waves-effect waves-light">
          Try again
        </S.Button>
      </S.ErrorBox>
    )
}

export default ErrorBox