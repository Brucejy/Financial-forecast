
# coding: utf-8

# In[1]:


import pandas as pd
import xgboost as xgb


# In[2]:


bgb=pd.read_excel("Balance Sheet.xls",'General Business')


# In[3]:


bb=pd.read_excel("Balance Sheet.xls",'Bank')


# In[4]:


bs=pd.read_excel("Balance Sheet.xls",'Securities')


# In[5]:


bi=pd.read_excel("Balance Sheet.xls",'Insurance')


# In[6]:


cgb=pd.read_excel("Cashflow Statement.xls",'General Business')


# In[7]:


cb=pd.read_excel("Cashflow Statement.xls",'Bank')


# In[8]:


cs=pd.read_excel("Cashflow Statement.xls",'Securities')


# In[9]:


ci=pd.read_excel("Cashflow Statement.xls",'Insurance')


# In[10]:


igb=pd.read_excel("Income Statement.xls",'General Business')


# In[11]:


ib=pd.read_excel("Income Statement.xls",'Bank')


# In[12]:


i_s=pd.read_excel("Income Statement.xls",'Securities')


# In[13]:


ii=pd.read_excel("Income Statement.xls",'Insurance')


# In[14]:


s=pd.read_csv("FDDC_financial_submit_20180524.csv",header=None)


# In[15]:


s.rename(columns={s.columns[0]:'ID'},inplace=True)


# In[16]:


del bgb['PARTY_ID'], bgb['MERGED_FLAG'], bb['PARTY_ID'], bb['MERGED_FLAG'], bs['PARTY_ID'], bs['MERGED_FLAG'], bi['PARTY_ID'], bi['MERGED_FLAG'], cgb['PARTY_ID'], cgb['MERGED_FLAG'], cb['PARTY_ID'], cb['MERGED_FLAG'], cs['PARTY_ID'], cs['MERGED_FLAG'], ci['PARTY_ID'], ci['MERGED_FLAG'], igb['PARTY_ID'], igb['MERGED_FLAG'], ib['PARTY_ID'], ib['MERGED_FLAG'], i_s['PARTY_ID'], i_s['MERGED_FLAG'], ii['PARTY_ID'], ii['MERGED_FLAG']


# In[17]:


bgb=bgb.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)
bb=bb.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)
bs=bs.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)
bi=bi.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)
cgb=cgb.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)
cb=cb.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)
cs=cs.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)
ci=ci.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)
igb=igb.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)
ib=ib.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)
i_s=i_s.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)
ii=ii.sort_values(['TICKER_SYMBOL','END_DATE']).reset_index(drop=True)


# In[18]:


bgb['ID']=bgb.TICKER_SYMBOL.astype(str)+'.'+bgb.EXCHANGE_CD
bgb.ID=bgb.ID.str.zfill(11)
bb['ID']=bb.TICKER_SYMBOL.astype(str)+'.'+bb.EXCHANGE_CD
bb.ID=bb.ID.str.zfill(11)
bs['ID']=bs.TICKER_SYMBOL.astype(str)+'.'+bs.EXCHANGE_CD
bs.ID=bs.ID.str.zfill(11)
bi['ID']=bi.TICKER_SYMBOL.astype(str)+'.'+bi.EXCHANGE_CD
bi.ID=bi.ID.str.zfill(11)


# In[19]:


cgb['ID']=cgb.TICKER_SYMBOL.astype(str)+'.'+cgb.EXCHANGE_CD
cgb.ID=cgb.ID.str.zfill(11)
cb['ID']=cb.TICKER_SYMBOL.astype(str)+'.'+cb.EXCHANGE_CD
cb.ID=cb.ID.str.zfill(11)
cs['ID']=cs.TICKER_SYMBOL.astype(str)+'.'+cs.EXCHANGE_CD
cs.ID=cs.ID.str.zfill(11)
ci['ID']=ci.TICKER_SYMBOL.astype(str)+'.'+ci.EXCHANGE_CD
ci.ID=ci.ID.str.zfill(11)


# In[20]:


igb['ID']=igb.TICKER_SYMBOL.astype(str)+'.'+igb.EXCHANGE_CD
igb.ID=igb.ID.str.zfill(11)
ib['ID']=ib.TICKER_SYMBOL.astype(str)+'.'+ib.EXCHANGE_CD
ib.ID=ib.ID.str.zfill(11)
i_s['ID']=i_s.TICKER_SYMBOL.astype(str)+'.'+i_s.EXCHANGE_CD
i_s.ID=i_s.ID.str.zfill(11)
ii['ID']=ii.TICKER_SYMBOL.astype(str)+'.'+ii.EXCHANGE_CD
ii.ID=ii.ID.str.zfill(11)


# In[21]:


bgbs=pd.merge(bgb,s,how='inner',on=['ID'])


# In[22]:


cgbs=pd.merge(cgb,s,how='inner',on=['ID'])


# In[23]:


igbs=pd.merge(igb,s,how='inner',on=['ID'])


# In[24]:


agbs0=pd.merge(bgbs,cgbs,how='inner',on=['TICKER_SYMBOL','EXCHANGE_CD','PUBLISH_DATE','END_DATE_REP','END_DATE','REPORT_TYPE','FISCAL_PERIOD','ID'])


# In[25]:


agbs=pd.merge(agbs0,igbs,how='inner',on=['TICKER_SYMBOL','EXCHANGE_CD','PUBLISH_DATE','END_DATE_REP','END_DATE','REPORT_TYPE','FISCAL_PERIOD','ID'])


# In[26]:


del agbs['TICKER_SYMBOL'],agbs['EXCHANGE_CD'],agbs['PUBLISH_DATE'],agbs['END_DATE_REP']


# In[27]:


ab0=pd.merge(bb,cb,how='inner',on=['TICKER_SYMBOL','EXCHANGE_CD','PUBLISH_DATE','END_DATE_REP','END_DATE','REPORT_TYPE','FISCAL_PERIOD','ID'])


# In[28]:


ab=pd.merge(ab0,ib,how='inner',on=['TICKER_SYMBOL','EXCHANGE_CD','PUBLISH_DATE','END_DATE_REP','END_DATE','REPORT_TYPE','FISCAL_PERIOD','ID'])


# In[29]:


del ab['TICKER_SYMBOL'],ab['EXCHANGE_CD'],ab['PUBLISH_DATE'],ab['END_DATE_REP']


# In[30]:


as0=pd.merge(bs,cs,how='inner',on=['TICKER_SYMBOL','EXCHANGE_CD','PUBLISH_DATE','END_DATE_REP','END_DATE','REPORT_TYPE','FISCAL_PERIOD','ID'])


# In[31]:


a_s=pd.merge(as0,i_s,how='inner',on=['TICKER_SYMBOL','EXCHANGE_CD','PUBLISH_DATE','END_DATE_REP','END_DATE','REPORT_TYPE','FISCAL_PERIOD','ID'])


# In[32]:


del a_s['TICKER_SYMBOL'],a_s['EXCHANGE_CD'],a_s['PUBLISH_DATE'],a_s['END_DATE_REP']


# In[33]:


ai0=pd.merge(bi,ci,how='inner',on=['TICKER_SYMBOL','EXCHANGE_CD','PUBLISH_DATE','END_DATE_REP','END_DATE','REPORT_TYPE','FISCAL_PERIOD','ID'])


# In[34]:


ai=pd.merge(ai0,ii,how='inner',on=['TICKER_SYMBOL','EXCHANGE_CD','PUBLISH_DATE','END_DATE_REP','END_DATE','REPORT_TYPE','FISCAL_PERIOD','ID'])


# In[35]:


del ai['TICKER_SYMBOL'],ai['EXCHANGE_CD'],ai['PUBLISH_DATE'],ai['END_DATE_REP']


# In[36]:


# For General Business part below
len(agbs.ID.drop_duplicates())


# In[37]:


gb6=agbs[agbs['FISCAL_PERIOD']==6]
gb61=gb6[gb6['END_DATE']=='2017-06-30']
gb61=gb61.drop_duplicates()
gb62=gb6[gb6['END_DATE']=='2016-06-30']
print(len(gb61.ID.drop_duplicates()))
print(len(gb62.ID.drop_duplicates()))


# In[38]:


gbcols=[col for col in gb6.columns if col in ['NOTES_RECEIV','AR','PREMIUM_RECEIV','REINSUR_RECEIV','INT_RECEIV','DIV_RECEIV','OTH_RECEIV','LT_RECEIV','ADVANCE_RECEIPTS','PREFERRED_STOCK_L','DEFER_REVENUE','OTH_EQUITY_INSTR','PREFERRED_STOCK_E','PERPETUAL_BOND_E','TREASURY_SHARE','OTH_COMPRE_INCOME','RETAINED_EARNINGS','FOREX_DIFFER','SEE','SEA','T_EQUITY_ATTR_P','MINORITY_INT','OTH_EFFECT_SE','OTH_EFFECT_SA','T_SH_EQUITY','C_FR_SALE_G_S','PREM_FR_ORIG_CONTR','N_REINSUR_PREM','IFC_CASH_INCR','REFUND_OF_TAX','C_FR_OTH_OPERATE_A','SPEC_OCIF','AOCIF','C_INF_FR_OPERATE_A','ANOCF','N_CF_OPERATE_A','GAIN_INVEST','N_DISP_SUBS_OTH_BIZ_C','C_FR_OTH_INVEST_A','SPEC_ICIF','AICIF','C_INF_FR_INVEST_A','ANICF','N_CF_FR_INVEST_A','FOREX_EFFECTS','OTH_EFFECT_CE','ACE','N_CHANGE_IN_CASH','N_CE_BEG_BAL','OTH_EFFECT_CEI','ACEI','N_CE_END_BAL','T_REVENUE','INT_INCOME','PREM_EARNED','COMMIS_INCOME','SPEC_TOR','ATOR','F_VALUE_CHG_GAIN','INVEST_INCOME','A_J_INVEST_INCOME','FOREX_GAIN','OTH_EFFECT_OP','AE_EFFECT_OP','OTH_GAIN','OPERATE_PROFIT','NOPERATE_INCOME','OTH_EFFECT_TP','AE_EFFECT_TP','T_PROFIT','OTH_EFFECT_NP','AE_EFFECT_NP','N_INCOME','GOING_CONCERN_NI','QUIT_CONCERN_NI','N_INCOME_ATTR_P','N_INCOME_BMA','MINORITY_GAIN','OTH_EFFECT_NPP','AE_EFFECT_NPP','BASIC_EPS','OTH_COMPR_INCOME','OTH_EFFECT_CI','AE_EFFECT_CI','T_COMPR_INCOME','COMPR_INC_ATTR_P','COMPR_INC_ATTR_M_S','OTH_EFFECT_PCI','AE_EFFECT_PCI'
]]


# In[39]:


xgb_tr=gb62[gbcols]
xgb_te=gb61[gbcols]


# In[40]:


model=xgb.XGBRegressor()


# In[41]:


model.fit(xgb_tr,gb62['REVENUE'])


# In[42]:


ygb_pred=model.predict(xgb_te)


# In[43]:


model.score(xgb_te,gb61['REVENUE'])


# In[44]:


fgbs=pd.DataFrame({'ID':gb61.ID,'y_pred':ygb_pred})


# In[45]:


fgbs=fgbs.drop_duplicates()


# In[46]:


fgbs=fgbs.reset_index(drop=True)


# In[47]:


fgbs=fgbs.drop([74,664,781,789,1210])


# In[48]:


fgbs.y_pred.isnull().value_counts()


# In[49]:


# For Bank part below
len(ab.ID.drop_duplicates())


# In[50]:


b12=ab[ab['FISCAL_PERIOD']==12]
b121=b12[b12['END_DATE']=='2017-12-31']
b122=b12[b12['END_DATE']=='2016-12-31']
print(len(b121.ID.drop_duplicates()))
print(len(b122.ID.drop_duplicates()))


# In[51]:


bcols=[col for col in b12.columns if col not in ['END_DATE','REPORT_TYPE','FISCAL_PERIOD','ID','REVENUE']]


# In[52]:


xb_tr=b122[bcols]
xb_te=b121[bcols]


# In[53]:


modelb=xgb.XGBRegressor()


# In[54]:


modelb.fit(xb_tr,b122['REVENUE'])


# In[55]:


yb_pred=modelb.predict(xb_te)


# In[56]:


modelb.score(xb_te,b121['REVENUE'])


# In[57]:


b3=ab[ab['FISCAL_PERIOD']==3]
b31=b3[b3['END_DATE']=='2018-03-31']
len(b3.ID.drop_duplicates())


# In[58]:


fb=pd.DataFrame({'ID':b121.ID.reset_index(drop=True),'y_pred':yb_pred/4+b31.REVENUE.reset_index(drop=True)})


# In[59]:


fbs=pd.merge(s,fb,how='inner',on=['ID'])


# In[60]:


#For Securities part below
len(a_s.ID.drop_duplicates())


# In[61]:


s12=a_s[a_s['FISCAL_PERIOD']==12]
s121=s12[s12['END_DATE']=='2017-12-31']
s122=s12[s12['END_DATE']=='2016-12-31']
print(len(s121.ID.drop_duplicates()))
print(len(s122.ID.drop_duplicates()))


# In[62]:


scols=[col for col in s12.columns if col not in ['END_DATE','REPORT_TYPE','FISCAL_PERIOD','ID','REVENUE']]


# In[63]:


xs_tr=s122[scols]
xs_te=s121[scols]


# In[64]:


models=xgb.XGBRegressor()


# In[65]:


models.fit(xs_tr,s122['REVENUE'])


# In[66]:


ys_pred=models.predict(xs_te)


# In[67]:


models.score(xs_te,s121['REVENUE'])


# In[68]:


fs=pd.DataFrame({'ID':s121.ID,'y_pred':ys_pred/2})


# In[69]:


fss=pd.merge(s,fs,how='inner',on=['ID'])


# In[70]:


#For Insurance part below
len(ai.ID.drop_duplicates())


# In[71]:


i12=ai[ai['FISCAL_PERIOD']==12]
i121=i12[i12['END_DATE']=='2017-12-31']
i122=i12[i12['END_DATE']=='2016-12-31']
print(len(i121.ID.drop_duplicates()))
print(len(i122.ID.drop_duplicates()))


# In[72]:


icols=[col for col in i12.columns if col not in ['END_DATE','REPORT_TYPE','FISCAL_PERIOD','ID','REVENUE']]


# In[73]:


xi_tr=i122[icols]
xi_te=i121[icols]


# In[74]:


modeli=xgb.XGBRegressor()


# In[75]:


modeli.fit(xi_tr,i122['REVENUE'])


# In[76]:


yi_pred=modeli.predict(xi_te)


# In[77]:


modeli.score(xi_te,i121['REVENUE'])


# In[78]:


fi=pd.DataFrame({'ID':i121.ID,'y_pred':yi_pred/2})


# In[79]:


fis=pd.merge(s,fi,how='inner',on=['ID'])


# In[80]:


m1=pd.merge(fss,fgbs,how="outer",on=['ID','y_pred'])
m2=pd.merge(m1,fbs,how="outer",on=['ID','y_pred'])
m3=pd.merge(m2,fis,how="outer",on=['ID','y_pred'])
m=pd.merge(s,m3,how="inner",on=['ID'])


# In[81]:


m=m.sort_values(['ID'])


# In[82]:


m.y_pred=round(m.y_pred/(10**6),2)


# In[83]:


m.y_pred.isnull().value_counts()


# In[84]:


m.to_csv("FDDC_financial_submit_20180810_010700.csv",header=None,index=False)

