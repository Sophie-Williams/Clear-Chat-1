#Find
	CHAT_WINDOW_WIDTH = 600
	
#Change
	if app.ENABLE_CLEAR_CHAT:
		CHAT_WINDOW_WIDTH = 620
	else:
		CHAT_WINDOW_WIDTH = 600
		
#Find
		chatInputSet.SetSize(550, 25)
		self.chatInputSet = chatInputSet
	
#Add
		if app.ENABLE_CLEAR_CHAT:
			self.btnClearChat = ui.Button()
			self.btnClearChat.SetParent(self)
			self.btnClearChat.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
			self.btnClearChat.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
			self.btnClearChat.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
			self.btnClearChat.SetToolTipText("Clear Chat")
			self.btnClearChat.SetEvent(lambda : chat.ClearChat())
			self.btnClearChat.Hide()
			
#Find
		self.btnSendWhisper = 0
		
#Add
		if app.ENABLE_CLEAR_CHAT:
			self.btnClearChat = 0
			
#Find
		self.btnSendWhisper.SetPosition(self.GetWidth() - 50, 2)
		self.btnSendWhisper.Show()
		
#Add
		if app.ENABLE_CLEAR_CHAT:
			self.btnClearChat.SetPosition(self.GetWidth() - 70, 2)
			self.btnClearChat.Show()
			
#Find
		self.btnSendWhisper.Hide()
		
#Add
		if app.ENABLE_CLEAR_CHAT:
			self.btnClearChat.Hide()