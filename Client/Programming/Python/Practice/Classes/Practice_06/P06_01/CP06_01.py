import os
import sys


# 회원
class CP06Member:
	# 생성자
	def __init__(self, a_oName: str, a_oPhoneNumber: str):
		self.m_oName = a_oName
		self.m_oPhoneNumber = a_oPhoneNumber
	
	# 정보를 출력한다
	def ShowInfo(self):
		print("이름 : {0}".format(self.m_oName))
		print("전화번호 : {0}".format(self.m_oPhoneNumber))


# 회원 관리자
class CP06MemberManager:
	m_oInst = None
	
	# 초기화
	def __init__(self):
		self.m_oMemberList = list()
		
		# 객체가 존재 할 경우
		if CP06MemberManager.m_oInst != None:
			raise Exception("CP06MemberManager.GetInst 메서드를 사용해주세요.")
		
		CP06MemberManager.m_oInst = self
	
	# 회원을 추가한다
	def AddMember(self, a_oMember: CP06Member):
		oMember = self.SearchMember(a_oMember.m_oName)
		
		# 회원이 없을 경우
		if oMember == None:
			self.m_oMemberList.append(a_oMember)
			return a_oMember
		
		return None
	
	# 회원을 제거한다
	def RemoveMember(self, a_oName: str):
		oMember = self.SearchMember(a_oName)
		
		# 회원이 존재 할 경우
		if oMember != None:
			self.m_oMemberList.remove(oMember)
			return oMember
		
		return None
	
	# 회원을 검색한다
	def SearchMember(self, a_oName: str):
		for oMember in self.m_oMemberList:
			# 이름이 동일 할 경우
			if oMember.m_oName == a_oName:
				return oMember
		
		return None
	
	# 모든 회원을 출력한다
	def PrintAllMembers(self):
		for oMember in self.m_oMemberList:
			oMember.ShowInfo()
			print()
	
	# 인스턴스를 반환한다
	@classmethod
	def GetInst(cls):
		# 객체 생성이 가능 할 경우
		if CP06MemberManager.m_oInst == None:
			CP06MemberManager.m_oInst = CP06MemberManager()
		
		return CP06MemberManager.m_oInst


# Practice 6 - 1
class CP06_01:
	MENU_NONE = -1
	MENU_ADD_MEMBER = 0
	MENU_REMOVE_MEMBER = 1
	MENU_SEARCH_MEMBER = 2
	MENU_PRINT_ALL_MEMBERS = 3
	MENU_EXIT = 4
	
	# 실행한다
	@classmethod
	def Run(cls):
		nSelMenu = cls.MENU_NONE
		
		while nSelMenu != cls.MENU_EXIT:
			cls.PrintMenu()
			nSelMenu = int(input("\n메뉴 선택 : ")) - 1
			
			# 회원 추가 일 경우
			if nSelMenu == cls.MENU_ADD_MEMBER:
				cls.AddMember()
			
			# 회원 삭제 일 경우
			elif nSelMenu == cls.MENU_REMOVE_MEMBER:
				cls.RemoveMember()
			
			# 회원 검색 일 경우
			elif nSelMenu == cls.MENU_SEARCH_MEMBER:
				cls.SearchMember()
			
			# 모든 회원 출력 일 경우
			elif nSelMenu == cls.MENU_PRINT_ALL_MEMBERS:
				cls.PrintAllMembers()
			
			print()
	
	# 메뉴를 출력한다
	@classmethod
	def PrintMenu(cls):
		print("=====> 메뉴 <=====")
		print("1. 회원 추가")
		print("2. 회원 삭제")
		print("3. 회원 검색")
		print("4. 모든 회원 출력")
		print("5. 종료")
	
	# 회원을 추가한다
	@classmethod
	def AddMember(cls):
		oName = input("이름 : ")
		oPhoneNumber = input("전화번호 : ")
		
		# 회원을 추가했을 경우
		if CP06MemberManager.GetInst().AddMember(CP06Member(oName, oPhoneNumber)) != None:
			print("\n{0} 을(를) 추가했습니다.".format(oName))
		else:
			print("\n{0} 은(는) 추가 된 회원입니다.".format(oName))
	
	# 회원을 삭제한다
	@classmethod
	def RemoveMember(cls):
		oName = input("이름 : ")
		
		# 회원을 삭제했을 경우
		if CP06MemberManager.GetInst().RemoveMember(oName) != None:
			print("\n{0} 을(를) 삭제했습니다.".format(oName))
		else:
			print("\n{0} 은(는) 없는 회원입니다.".format(oName))
	
	# 회원을 검색한다
	@classmethod
	def SearchMember(cls):
		oName = input("이름 : ")
		oMember = CP06MemberManager.GetInst().SearchMember(oName)
		
		# 회원이 존재 할 경우
		if oMember != None:
			print("\n=====> 회원 정보 <=====")
			oMember.ShowInfo()
		else:
			print("\n{0} 은(는) 없는 회원입니다.".format(oName))
	
	# 모든 회원을 출력한다
	@classmethod
	def PrintAllMembers(cls):
		print("=====> 모든 회원 정보 <=====")
		CP06MemberManager.GetInst().PrintAllMembers()
