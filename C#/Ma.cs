
//시트 전부 락걸음
private void SheetAllLock(FpSpread sprs)
{
    if(sprs.ActiveSheet.RowCount>0)
    {
        sprs.ActiveSheet.Cells[0, 0, sprs.ActiveSheet.RowCount - 1, sprs.ActiveSheet.ColumnCount - 1].Locked = true;
    }
}
